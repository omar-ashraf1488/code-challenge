from google.oauth2.service_account import Credentials

from api.weather_api import fetch_weather_data
from GCP.google_storage import create_bucket, create_folder
from GCP.google_bigQuery import insert_row_into_bigquery
from GCP.bigQuery_query_dump import dump_ingested_data
from utilis.index import get_user_inputs
from config import Config


def main(config:Config):
    # Fetch weather data
    weather_data = fetch_weather_data(config.api_location, config.start_date, config.end_date ,config.api_key)

    # Create a bucket in Google Cloud
    create_bucket(credentials=config.credentials, project_name=config.project_name, bucket_name=config.bucket_name, location=config.service_location)

    # Create a folder in Google Cloud
    create_folder(credentials=config.credentials, project_name=config.project_name, bucket_name=config.bucket_name, folder_name=config.folder_name)

    # Insert weather data into BigQuery
    id = insert_row_into_bigquery(credentials=config.credentials,target_table=config.target_table, row_to_insert=weather_data)

    # Dump the ingested data from BigQuery
    dump_ingested_data(credentials=config.credentials, target_table=config.target_table, id=id)
    
if __name__ == '__main__':
    user_inputs = get_user_inputs()
    
    credentials_path = user_inputs['credentials_path']
    target_table = user_inputs['big_query_target_id'] 
    api_key = user_inputs['api_key'] 
    start_date = user_inputs['start_date'] 
    end_date = user_inputs['end_date'] 
    location = user_inputs['location']

    # Note: The following code is for solving the challenge and not follow best practices for production use.
    service_location = 'europe-west3'
    project_name = 'code-challenge-tagesspiegel'
    bucket_name = 'weather-data-bucket1'
    folder_name = 'weather-data'

    # Load credentials from the JSON key file
    credentials = Credentials.from_service_account_file(credentials_path)

    config = Config(credentials, target_table, api_key,start_date, end_date, service_location, location,
                    project_name, bucket_name, folder_name)

    main(config)