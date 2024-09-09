docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="NYC_taxi" \
  -v /Users/marcinmajeran/Public/Stuff/DE/data-engineering-zoomcamp/00-my-practice/01-docker-terraform-homework/ny_taxi_postgres_data:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network=pg-network \
  --name pg-database \
  postgres:13
