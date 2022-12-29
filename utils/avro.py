from numpy import int64
import pandas as pd
from fastavro import writer, reader, parse_schema
import numpy as np
from utils import aws, secrets
from config import schema


config = secrets.read_secrets_from_config()

log_bucket = config.get("LOG_BUCKET")
raw_bucket = config.get("RAW_BUCKET")


def select_schema(filename):
    match filename:
        case "hired_employees":
            return schema.hired_employees_schema, schema.hired_employees_columns

        case "departments":
            return schema.departments_schema, schema.departments_columns

        case "jobs":
            return schema.jobs_schema, schema.jobs_columns
        case _:
            return "", ""


def upload_file(df, file_name, verified_records):
    if verified_records:
        msg = write_temp_file(df, file_name, verified_records)
        if msg is not None:
            return msg
        else:
            print(msg)
        aws.upload_file_to_s3(file_name + ".avro", raw_bucket)
    else:
        write_temp_file(df, file_name, verified_records)
        aws.upload_file_to_s3(file_name + "_log.csv", log_bucket)
    return None


def write_temp_file(df, file_name, verified_records):
    schema, columns = select_schema(file_name)
    if schema == "":
        return "there is no schema asociated to filename"
    df.columns = columns
    if verified_records:
        records = df.to_dict("records")
        parsed_schema = parse_schema(schema)
        with open(file_name + ".avro", "wb") as out:
            writer(out, parsed_schema, records)
    else:
        df.astype(str)
        df.to_csv(file_name + "_log.csv")
    return None


def read_avro_file(file_name):
    avro_records = []
    with open(file_name + '.avro', 'rb') as fo:
        avro_reader = reader(fo)
        for record in avro_reader:
            avro_records.append(record)
    df_avro = pd.DataFrame(avro_records)
    return df_avro
