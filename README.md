# Code Challenge

## Description

This service retrieves weather data from a weather API and ingests it into Google BigQuery and Google Cloud Storage. 


## Prerequisites

- Python 3 or a higher version
- Dependencies and access the weather API, Google BigQuery, and Google Cloud Storage.
- The required input parameters (for retrieving and storing the weather data):
     - START_DATE, 
     - END_DATE, 
     - LOCATION, 
     - API_KEY, 
     - GOOGLE_APPLICATION_CREDENTIALS_PATH
     - BIG_QUERY_TARGET_ID

## Configuration
Open the <code>main.py</code> file in a text editor.

Modify the following variables based on your requirements:

```python
service_location = ''
project_name = ''
bucket_name = ''
folder_name = ''
```
Note: 
- Hard-coded the above variables is not considered best practice, but you can customize them to suit your service.
- Create a new dataset by providing a name and selecting the appropriate location.

- Within the newly created dataset, create a new table by specifying the schema and table name.


## Running the Service
- Run the mac-starter.sh script by executing the following command:

```bash
bash mac-starter.sh
```

Note: If you are not using macOS, modify the script accordingly for your operating system.

Provide the required inputs:

- START_DATE: Enter the start date in the format "YYYY-MM-DD".
- END_DATE: Enter the end date in the format "YYYY-MM-DD".
- LOCATION: Enter the location as a string.
- API_KEY: Enter your API key as a string.
- GOOGLE_APPLICATION_CREDENTIALS_PATH: Enter the file path to your Google Application Credentials as a string.
- BIG_QUERY_TARGET_ID: Enter the target BigQuery table ID in the format "PROJECT.DATASET.TABLE".

Once finished, you should see a result similar to the following:

```yaml
Dumping the result:
resolved_address: Oslo, Norge
start_date: 2023-05-15
queryCost: 1
temp: 13.9
cloudcover: 88.1
datetimeEpoch: 2023-05-14 22:00:00+00:00
created_at: 2023-05-15 00:06:40.174907+00:00
weather_uuid: 376a9c38-1f1b-435c-8fe0-e6c24ec993e6
```
## Overview of Data Flow in the Project
The diagram will provide an overview of how data moves through different components of the project.

<p align="center">
<img src="Pipeline Diagram.drawio.png" alt="Pipeline Diagram" width="50%">
</p>