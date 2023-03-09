# %%
import pandas as pd
import numpy as np

from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning

# creates class instances
db_connector = DatabaseConnector()
data_extractor = DataExtractor()
data_cleaner = DataCleaning()

# %%

# get name of the table containing user data
tables = db_connector.list_db_tables()
print(tables)
# %%

# extract table containing user data and return DataFrame
user_df = data_extractor.read_rds_table(db_connector, 'legacy_users')

# clean the user data
clean_user_df = data_cleaner.clean_user_data(user_df)

# upload the user data to the 'Sales_Data' database
db_connector.upload_to_db(clean_user_df, 'dim_users')
# %%

# extract data from PDF document and return DataFrame
pdf_df = data_extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')

# clean the PDF data
clean_pdf_df = data_cleaner.clean_card_data(pdf_df)

# upload the card data to the 'Sales_Data' database
db_connector.upload_to_db(clean_pdf_df, 'dim_card_details')

# %%

# using API extract number of stores
data_extractor.list_number_of_stores('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores', {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'})

# using API extract store data and return DataFrame
stores_df = data_extractor.retrieve_stores_data('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/', {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'})

# clean the stores data
clean_stores_df = data_cleaner.called_clean_store_data(stores_df)

# upload the store data to the 'Sales_Data' database
db_connector.upload_to_db(clean_stores_df, 'dim_store_details')
# %%

# extract products data from s3 bucket
products_df = data_extractor.extract_from_s3('s3://data-handling-public/products.csv')

# clean the products data
products_df = data_cleaner.convert_product_weights(products_df)
clean_products_df = data_cleaner.clean_products_data(products_df)

# upload the products data to the 'Sales_Data' database
db_connector.upload_to_db(clean_products_df, 'dim_products')
# %%

# extract table containing order data and return DataFrame
orders_df = data_extractor.read_rds_table(db_connector, 'orders_table')

# clean the orders data
clean_orders_df = data_cleaner.clean_orders_data(orders_df)

# upload the orders data to the Sales_Data database
db_connector.upload_to_db(clean_orders_df, 'orders_table')