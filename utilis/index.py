import sys

def get_user_inputs():
    return {
        'start_date': sys.argv[1],
        'end_date': sys.argv[2],
        'location': sys.argv[3],
        'api_key': sys.argv[4],
        'credentials_path': sys.argv[5],
        'big_query_target_id': sys.argv[6]
    }