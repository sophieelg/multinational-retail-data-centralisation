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

        # update index column
        stores_df = stores_df.reset_index(drop=True)
        return stores_df
    
    def clean_products_data(self, products_df):
        # remove NULL and duplicates
        products_df.replace('NULL', np.nan, inplace=True)
        products_df.dropna(inplace=True)
        products_df.drop_duplicates(inplace=True)

        # remove and update incorrect data
        products_df = products_df[products_df['category'].isin(['toys-and-games', 'sports-and-leisure', 'pets', 'homeware', 'health-and-beauty', 'food-and-drink', 'diy'])]

        # correct date values
        products_df['date_added'] = pd.to_datetime(products_df['date_added'], infer_datetime_format=True, errors='coerce')

        # change dtypes
        products_df['product_price'] = products_df['product_price'].str.replace('£', '')
        products_df['product_price'] = products_df['product_price'].astype('float')
        products_df['category'] = products_df['category'].astype('category')
        products_df['removed'] = products_df['removed'].astype('category')

        # update index column
        products_df.drop('Unnamed: 0', axis=1, inplace=True)
        products_df = products_df.reset_index(drop=True)
        return products_df
    
    def convert_product_weights(self, products_df):
        # create new column which extacts the weight amount
        products_df['weight_amount'] = products_df['weight'].str.replace(r'[^\d.]+', '')
        products_df['weight_amount'] = pd.to_numeric(products_df['weight_amount'])
        products_df['weight_amount'] = products_df['weight_amount'].astype('float')

        # create new column which extract the weight unit
        products_df['weight_unit'] = products_df.weight.str.replace('[^a-zA-Z]', '')
        products_df['weight_unit'] = products_df['weight_unit'].astype('str')

        # update incorrect unit
        unit_mapping = {'xg' : 'g'}
        products_df.replace({"weight_unit": unit_mapping}, inplace=True)

        # convert weight to kg based on unit
        products_df.loc[products_df['weight_unit'] == 'g', 'weight_amount'] /= 1000
        products_df.loc[products_df['weight_unit'] == 'ml', 'weight_amount'] /= 1000
        products_df.loc[products_df['weight_unit'] == 'oz', 'weight_amount'] /= 35.274

        # replace weight column and remove extra columns
        products_df['weight'] = products_df['weight_amount']
        products_df.rename(columns={'weight': 'weight(kg)'}, inplace=True)
        products_df.drop(['weight_amount', 'weight_unit'], axis=1, inplace=True)
        return products_df
    
    def clean_orders_data(self, orders_df):
        # remove columns
        orders_df.drop(['first_name', 'last_name', '1', 'level_0'], axis=1, inplace=True)
        return orders_df
    
    def clean_date_events_data(self, date_events_df):
        # remove NULL and duplicates
        date_events_df.replace('NULL', np.nan, inplace=True)
        date_events_df.dropna(inplace=True)
        date_events_df.drop_duplicates(inplace=True)

        # remove and update incorrect data
        date_events_df = date_events_df[date_events_df['time_period'].isin(['Evening', 'Morning', 'Midday', 'Late_Hours'])]

        # change dtype
        date_events_df['time_period'] = date_events_df['time_period'].astype('category')
        return date_events_df
# %%
