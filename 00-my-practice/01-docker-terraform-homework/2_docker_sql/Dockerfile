FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app
COPY data-ingest.py data-ingest.py

ENTRYPOINT [ "python", "data-ingest.py" ]

