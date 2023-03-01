# %%
import numpy as np
import pandas as pd
# %%

class DataCleaning:
    def clean_user_data(self, user_df):
        # remove NULL & duplicates
        user_df.replace('NULL', np.nan, inplace=True)
        user_df.dropna(inplace=True)
        user_df.drop_duplicates(inplace=True)

        # remove incorrect data
        user_df = user_df[user_df['country_code'].isin(['DE', 'GB', 'US'])]

        # correct date values
        user_df['date_of_birth'] = pd.to_datetime(user_df['date_of_birth'], infer_datetime_format=True, errors='coerce')
        user_df['join_date'] = pd.to_datetime(user_df['join_date'], infer_datetime_format=True, errors='coerce')
        return user_df

# %%
