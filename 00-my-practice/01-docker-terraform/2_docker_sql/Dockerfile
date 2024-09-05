FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app
COPY upload-data.py upload-data.py

ENTRYPOINT [ "python", "upload-data.py" ]
