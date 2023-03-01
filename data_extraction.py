# %%
import pandas as pd
import database_utils
import numpy as np

# %%

class DataExtractor:
    def read_rds_table(self, db_connector, table_name):
        engine = db_connector.init_db_engine()
        user_data = pd.read_sql_table(table_name, engine, index_col='index')
        return user_data

# %%
