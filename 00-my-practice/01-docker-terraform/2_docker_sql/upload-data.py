import pandas as pd
import pyarrow.parquet as pq
import argparse
import os
from sqlalchemy import create_engine
import psycopg2

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = 'output.parquet'
    
    os.system(f'wget {url} -O {parquet_name}')

    df_pq = pq.ParquetFile(parquet_name)
    df = pd.DataFrame()
    # THIS IS POINTLESS
    for batch in df_pq.iter_batches():
#        print('batch ingesting...')
        df = pd.concat([df, batch.to_pandas()])

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    df.head(0).to_sql(con=engine, name=table_name, if_exists='replace')
    df.head(10).to_sql(con=engine, name=table_name, if_exists='append')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingesting the data')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres') 
    parser.add_argument('--host', help='host for postgres') 
    parser.add_argument('--port', help='port for postgres') 
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the tablewhere we will write the results')
    parser.add_argument('--url', help='url of thge csv file')
     
    args = parser.parse_args()

    main(args)
