import requests
import json
import duckdb
import dlt


import dlt
import duckdb

data = [
    {
        "vendor_name": "VTS",
				"record_hash": "b00361a396177a9cb410ff61f20015ad",
        "time": {
            "pickup": "2009-06-14 23:23:00",
            "dropoff": "2009-06-14 23:48:00"
        },
        "Trip_Distance": 17.52,
        # nested dictionaries could be flattened
        "coordinates": { # coordinates__start__lon
            "start": {
                "lon": -73.787442,
                "lat": 40.641525
            },
            "end": {
                "lon": -73.980072,
                "lat": 40.742963
            }
        },
        "Rate_Code": None,
        "store_and_forward": None,
        "Payment": {
            "type": "Credit",
            "amt": 20.5,
            "surcharge": 0,
            "mta_tax": None,
            "tip": 9,
            "tolls": 4.15,
						"status": "booked"
        },
        "Passenger_Count": 2,
        # nested lists need to be expressed as separate tables
        "passengers": [
            {"name": "John", "rating": 4.9},
            {"name": "Jack", "rating": 3.9}
        ],
        "Stops": [
            {"lon": -73.6, "lat": 40.6},
            {"lon": -73.5, "lat": 40.5}
        ]
    },
    # ... more data
]

pipeline = dlt.pipeline(destination='duckdb',
                        dataset_name='normalised_rides',
                          pipelines_dir='00-my-practice/workshop-1/pipelines/')

info = pipeline.run(data,
                    table_name="normalised_exercise",
                    write_disposition="merge",
                    primary_key="record_hash")

print(info)

con = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")
con.sql(f"SET search_path = '{pipeline.dataset_name}'")
print('Loaded tables: ')
print(con.sql('show tables'))
print(con.sql('SELECT * FROM normalised_rides.normalised_exercise LIMIT 1'))