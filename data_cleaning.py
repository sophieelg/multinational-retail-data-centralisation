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
    
    def clean_card_data(self, pdf_df):
        # format data
        pdf_df['card_number'] = pdf_df['card_number'].str.replace(r'[^0-9]+', '')

        # remove NULL & duplicates
        pdf_df.replace('NULL', np.nan, inplace=True)
        pdf_df.dropna(inplace=True)
        pdf_df.drop_duplicates(inplace=True)

        # remove incorrect data
        pdf_df = pdf_df[pdf_df['card_provider'].isin(['Diners Club / Carte Blanche', 'American Express', 'JCB 16 digit', 'JCB 15 digit', 'Maestro', 'Mastercard', 'Discover', 'VISA 19 digit', 'VISA 16 digit', 'VISA 13 digit'])]
        
        # correct date values
        pdf_df['expiry_date'] = pd.to_datetime(pdf_df['expiry_date'], format='%m/%y')
        pdf_df['date_payment_confirmed'] = pd.to_datetime(pdf_df['date_payment_confirmed'], infer_datetime_format=True, errors='coerce')

        # change dtypes
        pdf_df['card_number'] = pdf_df['card_number'].astype('int')
        pdf_df['card_provider'] = pdf_df['card_provider'].astype('category')
        return pdf_df
    
    def called_clean_store_data(self, stores_df):
        # drop lat column
        stores_df.drop(['lat'], axis=1, inplace=True)

        # format data
        stores_df['staff_numbers'] = stores_df['staff_numbers'].str.replace(r'[^0-9]+', '')

        # remove NULL and duplicates
        stores_df.replace('NULL', np.nan, inplace=True)
        stores_df.dropna(inplace=True)
        stores_df.drop_duplicates(inplace=True)

        # remove and update incorrect data
        stores_df = stores_df[stores_df['country_code'].isin(['DE', 'GB', 'US'])]
        continent_mapping = {'eeEurope' : 'Europe', 'eeAmerica' : 'America'}
        stores_df.replace({"continent": continent_mapping}, inplace=True)

        # correct date values
        stores_df['opening_date'] = pd.to_datetime(stores_df['opening_date'], infer_datetime_format=True, errors='coerce')

        # change dtypes
        stores_df['longitude'] = stores_df['longitude'].astype('float')
        stores_df['staff_numbers'] = stores_df['staff_numbers'].astype('int')
        stores_df['store_type'] = stores_df['store_type'].astype('category')
        stores_df['latitude'] = stores_df['latitude'].astype('float')
        stores_df['country_code'] = stores_df['country_code'].astype('category')
        stores_df['continent'] = stores_df['continent'].astype('category')
        return stores_df





# %%
