# data_lake_service
APIs to ingest data and perform some analytics task


![Alt text](img/architecture.png?raw=true "Title")

## Running Local

1. To test locally you will need to fill the config parrameters in /config/app/config.yaml
2. Run `python app.py`

## Running with Docker

1. `docker build . -t datalake-service`
2. `docker run -it -p 8080:8080 datalake-service`

## API Doc
1. To check the API documentation you can open the swagger file using visualcode extension "Swagger viewer", the file is located in /static/swagger/swagger.yaml , or visit the webpage http://0.0.0.0:8080/swagger while running locally.