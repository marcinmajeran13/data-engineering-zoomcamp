import pandas as pd
import pyarrow.parquet as pq
import argparse
import os
from sqlalchemy import create_engine
import psycopg2

def main(params):
    user = params.user
    password = params.password
    db = params.db
    port = params.port
    host = params.host
    table = params.table
    url = params.url
    
    data_name = 'data.parquet'
    
    os.system(f'wget {url} -O {data_name}')
    df_pq = pq.ParquetFile(data_name)          
    df = pd.DataFrame()


    for batch in df_pq.iter_batches():
    #        print('batch ingesting...')
        df = pd.concat([df, batch.to_pandas()])

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    df.head(0).to_sql(con=engine, name=table, if_exists='replace')
    df.to_sql(con=engine, name=table, if_exists='append', chunksize=100000)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ingesting the data...')
              
    parser.add_argument('--user')
    parser.add_argument('--password')
    parser.add_argument('--db')
    parser.add_argument('--port')
    parser.add_argument('--host')
    parser.add_argument('--table')
    parser.add_argument('--url')
    
    args = parser.parse_args()
    main(args)
