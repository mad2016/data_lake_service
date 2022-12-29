import re
from flask import (
    Flask,
    request,
    make_response,
    render_template,
    flash,
    redirect,
    url_for,
)

# from appmap.flask import AppmapFlask
from flask_jwt_extended import JWTManager, jwt_required
import logging
import json
import os
import pandas as pd
from data_gov import rules
from utils import avro, aws, secrets
import numpy as np


app = Flask(__name__)
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["CACHE_TYPE"] = "SimpleCache"
app.config["CACHE_DEFAULT_TIMEOUT"] = 3600
jwt = JWTManager(app)


config = secrets.read_secrets_from_config()

source_bucket = config.get("SOURCE_BUCKET")
raw_bucket = config.get("RAW_BUCKET")


@app.route("/swagger")
def get_docs():
    print("sending docs")
    return render_template("swaggerui.html")


@app.route("/v1/healthz", methods=["GET"])
def health_check():
    return make_response({"ok": True, "message": "Service Healthy!"}, 200)


@app.route("/v1/load", methods=["GET"])
def load_data():
    keys = aws.get_file_names(source_bucket)
    print(keys)
    for key in keys:
        filename = os.path.basename(key).split('.')[0]
        df = aws.read_csv_to_pandas(source_bucket, os.path.basename(key))
        df = df.convert_dtypes()
        null_rows_df, not_null_rows_df = rules.split_nulls(df)
        # send file to raw bucket
        err = avro.upload_file(null_rows_df, filename, False)
        if err is not None:
            return make_response({"Error": True, "msg": err}, 400)
        # send file to log bucket
        avro.upload_file(not_null_rows_df, filename, True)

        # sync file to redshift
        aws.sync_s3_to_redshift(raw_bucket, filename)

        if err is not None:
            return make_response({"Error": True, "msg": err}, 400)
    return make_response({"OK": True, "msg": "Process Finished!"}, 200)


@app.route("/v1/admin", methods=["GET"])
@jwt_required()
def admin():
    return make_response({"ok": True, "message": "Service Healthy!"}, 200)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080, threaded=True)
