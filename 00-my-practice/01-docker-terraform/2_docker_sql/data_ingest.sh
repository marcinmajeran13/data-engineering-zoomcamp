URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet" \

docker run -it  \
  --network=pg-network \
  ingest_taxi:v002 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url=${URL} \

