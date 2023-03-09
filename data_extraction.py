# %%
import pandas as pd
import numpy as np
import tabula
import requests
import boto3

# %%

class DataExtractor:
    def read_rds_table(self, db_connector, table_name):
        engine = db_connector.init_db_engine()
        user_data = pd.read_sql_table(table_name, engine, index_col='index')
        return user_data
    
    def retrieve_pdf_data(self, link):
        pdf_df = pd.concat(tabula.read_pdf(link, pages='all'), ignore_index=True)
        return pdf_df
    
    def list_number_of_stores(self, stores_endpoint, header_dict):
        response = requests.get(stores_endpoint, headers=header_dict)
        number_of_stores = response.json()
        return number_of_stores
    
    def retrieve_stores_data(self, retrieve_stores_endpoint, header_dict):
        stores_data_list = []
        for i in range(451):
            response = requests.get(retrieve_stores_endpoint + str(i), headers=header_dict)
            stores_data = response.json()
            df = pd.DataFrame(stores_data, index=[i])
            stores_data_list.append(df)
            stores_df = pd.concat(stores_data_list, ignore_index=True)
        return stores_df
    
    def extract_from_s3(self, s3_url):
        s3_client = boto3.client('s3')
        product_df = pd.read_csv(s3_url)
        return product_df

        

# %%
