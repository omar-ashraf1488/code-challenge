from google.cloud import bigquery

def dump_ingested_data(credentials,target_table, id):
    try:
        # Initialize BigQuery client
        client = bigquery.Client(credentials=credentials)
        QUERY = (
            f'SELECT * FROM `{target_table}` '
            f"WHERE weather_uuid = '{id}'"
            'LIMIT 1'
        )

        query_job = client.query(QUERY)  # API request
        rows = query_job.result()  # Waits for query to finish

        result = {}
        for row in rows:
            row_dict = dict(row.items())
            result.update(row_dict)
        print("\n" + "\033[32m" + "Dumping the result:" + "\033[0m")

        for k, v in result.items():
            print(f"{k}: {v}")

        return result
    except Exception as e:
        print(f"An error occurred while dumping data from BigQuery: {e}")
