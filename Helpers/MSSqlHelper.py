import math

import requests
from Helpers.SqlLiteHelper import SQLiteHelper


class MSSqlHelper:
    def __init__(self):
        url = "http://108.181.167.26:8080/AddParts"

    def _insert_many_records(self, records):
        page_size = 10000
        total_length = len(records)
        num_pages = math.ceil(total_length / page_size)

        for i in range(num_pages):
            start_index = i * page_size
            end_index = start_index + page_size
            chunk_records = records[start_index:end_index]
            response = requests.post(self.url, json=chunk_records)
            if response.status_code != 200:
                raise Exception(
                    f"Failed to add records {start_index} to {end_index}. Status Code: {response.status_code}"
                )
            print(f"{end_index} are added into global database")
