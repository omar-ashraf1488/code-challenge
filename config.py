
class Config:
    def __init__(self, credentials, target_table, api_key, start_date, end_date, service_location, api_location,
                 project_name, bucket_name, folder_name):
        self.credentials = credentials
        self.target_table = target_table
        self.api_key = api_key
        self.start_date = start_date
        self.end_date = end_date
        self.api_location = api_location
        self. service_location =  service_location
        self.project_name = project_name
        self.bucket_name = bucket_name
        self.folder_name = folder_name




