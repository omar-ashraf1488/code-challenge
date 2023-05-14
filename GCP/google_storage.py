from google.cloud import storage
from google.cloud.exceptions import Conflict


def create_bucket(credentials, project_name, bucket_name, location):
    storage_client = storage.Client(project=project_name, credentials=credentials)
    try:
    # Create the bucket in the specified location
        bucket = storage_client.create_bucket(bucket_or_name=bucket_name, project=project_name, location=location, timeout=5)
        print(f"Bucket '{bucket.name}' created in location '{location}'.")
    except Conflict:
        print(f"Bucket '{bucket_name}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_folder(credentials, project_name, bucket_name, folder_name):

    # Instantiate the storage client
    storage_client = storage.Client(project=project_name, credentials=credentials)

    # Specify the object name with the folder prefix
    object_name = folder_name + "/"  # Add a trailing slash to indicate a folder

     # Upload an empty object to create the "folder"
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    try:
        if blob.exists():
            print(f"Folder '{folder_name}' already exists in bucket '{bucket_name}'.")
        else:
            # Upload an empty object to create the "folder"
            blob.upload_from_string("")
            print(f"Folder '{folder_name}' created in bucket '{bucket_name}'.")

    except Exception as e:
        print(f"An error occurred while creating folder in bucket '{bucket_name}': {e}")

