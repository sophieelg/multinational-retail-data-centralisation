# %%
from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
# %%

# creates class instances
db_connector = DatabaseConnector()
data_extractor = DataExtractor()
data_cleaner = DataCleaning()

# %%

# get name of the table containing user data
tables = db_connector.list_db_tables()
print(tables)

# extract table containing user data and return pandas DataFrame
user_df = data_extractor.read_rds_table(db_connector, 'legacy_users')

# clean the user data
user_df = data_cleaner.clean_user_data(user_df)

# store the data in 'Sales_Data' database
db_connector.upload_to_db(user_df)
# %%
