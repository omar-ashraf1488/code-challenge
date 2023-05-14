from google.cloud import bigquery

def dump_ingested_data(credentials,target_table, start_date):
    try:
        # Initialize BigQuery client
        client = bigquery.Client(credentials=credentials)
        QUERY = (
            f'SELECT * FROM `{target_table}` '
            f'WHERE start_date = "{start_date}" '
            'ORDER BY start_date DESC '
            'LIMIT 1'
        )

        query_job = client.query(QUERY)  # API request
        rows = query_job.result()  # Waits for query to finish

        result = {}
        for row in rows:
            row_dict = dict(row.items())
            result.update(row_dict)
        print("Dumping the result:")
        print(result)

        return result
    except Exception as e:
        print(f"An error occurred while dumping data from BigQuery: {e}")
