import requests
import dlt
import os
import duckdb

BASE_API_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"

pipeline = dlt.pipeline(pipeline_name='taxi_data',
                        destination='duckdb',
                        dataset_name='taxi_rides',
                        pipelines_dir='00-my-practice/workshop-1/pipelines/')

def paginated_getter():
    page_number = 1

    while page_number==1:
        params = {'page': page_number}

        response = requests.get(BASE_API_URL, params=params)
        response.raise_for_status()
        page_json = response.json()
        print(f'got page number {page_number} with {len(page_json)} records')

        if page_json:
            yield page_json
            page_number += 1
        else:
            break
        
data = paginated_getter()

info = pipeline.run(data,
                    table_name='taxi_rides',
                    write_disposition='replace')

print(info)
    
con = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")
con.sql(f"SET search_path = '{pipeline.dataset_name}'")
print('Loaded tables: ')
print(con.sql('show tables'))

rides = con.sql(
    """
    WITH cte AS (
        SELECT
            MAX(end_lat) as end_lat
        FROM
            taxi_rides.taxi_rides
    )
    SELECT
        *
    FROM 
        taxi_rides.taxi_rides
        JOIN  cte USING (end_lat)
    """
).df()
print(rides)
