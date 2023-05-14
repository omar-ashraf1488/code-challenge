from google.cloud import bigquery
import json

def insert_row_into_bigquery(credentials, target_table, row_to_insert):
    try:
        # Initialize BigQuery client
        client = bigquery.Client(credentials=credentials)

        # Extract project name, dataset ID, and table ID from target table
        project_name, dataset_id, table_id = target_table.split('.')

        # Get dataset and table references
        dataset_ref = client.dataset(dataset_id, project=project_name)
        table_ref = dataset_ref.table(table_id)

        # Get the table object
        table = client.get_table(table_ref)

        # Insert row into the table
        errors = client.insert_rows(table, [row_to_insert])

        for err in errors:
            print('\n' + err['reason'])
            print('\n' + err['message'] + '\n')

        if errors:
            raise Exception(f"Errors occurred while inserting row into BigQuery: {errors}")
        else:
            return row_to_insert[-1]
    except Exception as e:
        print(f"An error occurred while inserting row into BigQuery: {e}")