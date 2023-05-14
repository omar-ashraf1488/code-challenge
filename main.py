from google.oauth2.service_account import Credentials

from weather_api import fetch_weather_data
from GCP.google_storage import create_bucket, create_folder
from GCP.google_bigQuery import insert_row_into_bigquery
from GCP.bigQuery_query_dump import dump_ingested_data
from config import Config


def main(config:Config):
    # Fetch weather data
    weather_data = fetch_weather_data(config.api_location, config.start_date, config.end_date ,config.api_key)

    # Create a bucket in Google Cloud
    create_bucket(credentials=config.credentials, project_name=config.project_name, bucket_name=config.bucket_name, location=config.service_location)

    # Create a folder in Google Cloud
    create_folder(credentials=config.credentials, project_name=config.project_name, bucket_name=config.bucket_name, folder_name=config.folder_name)

    # Insert weather data into BigQuery
    insert_row_into_bigquery(credentials=config.credentials,target_table=config.target_table, row_to_insert=weather_data)

    # Dump the ingested data from BigQuery
    dump_ingested_data(credentials=config.credentials, target_table=config.target_table, start_date=config.start_date)
    
if __name__ == '__main__':

    # Note: The following code is for solving the challenge and not follow best practices for production use.
    credentials_path = './env/code-challenge-tagesspiegel-d48fd3f5e794.json'
    target_table = 'code-challenge-tagesspiegel.code_challenge_tagesspiegel_dataset.code_challenge_tagesspiegel_table'
    api_key = 'L5YEW6VYK2RQJLXD9BUJZTCYH'
    start_date = '2023-05-12'
    end_date = ''
    location = 'Berlin'

    service_location = 'europe-west3'
    project_name = 'code-challenge-tagesspiegel'
    bucket_name = 'weather-data-bucket1'
    folder_name = 'weather-data'

    # Load credentials from the JSON key file
    credentials = Credentials.from_service_account_file(credentials_path)

    config = Config(credentials, target_table, api_key,start_date, end_date, service_location, location,
                    project_name, bucket_name, folder_name)

    main(config)