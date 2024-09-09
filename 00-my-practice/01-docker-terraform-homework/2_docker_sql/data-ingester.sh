URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet" \

docker run -it \
  --network=pg-network \
  data-ingester:v002 \
    --user=root \
    --password=root \
    --db=NYC_taxi \
    --host=pg-database \
    --port=5432 \
    --table=yellow_taxi \
    --url=${URL} \
