# %%
import yaml
from sqlalchemy import create_engine, inspect
import pandas as pd

# %%
class DatabaseConnector:
    def read_db_creds(self, file):
        with open(file, 'r') as file:
            credentials = yaml.safe_load(file)
        return credentials
    
    def init_db_engine(self):
        credentials = self.read_db_creds('db_creds.yaml')
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = credentials['RDS_HOST']
        USER = credentials['RDS_USER']
        PASSWORD = credentials['RDS_PASSWORD']
        DATABASE = credentials['RDS_DATABASE']
        PORT = credentials['RDS_PORT']
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        return engine

    def list_db_tables(self):
        engine = self.init_db_engine()
        inspector = inspect(engine)
        tables_names = inspector.get_table_names()
        return tables_names
    
    def upload_to_db(self, df, table_name):
        credentials = self.read_db_creds('local_db_creds.yaml')
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = credentials['LOCAL_HOST']
        USER = credentials['LOCAL_USER']
        PASSWORD = credentials['LOCAL_PASSWORD']
        DATABASE = credentials['LOCAL_DATABASE']
        PORT = credentials['LOCAL_PORT']
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        engine.connect()
        df.to_sql(name=table_name, con=engine, if_exists='replace')

# %%
