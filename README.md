# Multinational Retail Centralisation

Scenario: You work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team. In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location. Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data. You will then query the database to get up-to-date metrics for the business.

## Milestone 1

- Set up of the dev environment.

## Milestone 2

- Extracted and cleaned the data from multiple data sources;
  - AWS database

```python
class DataExtractor:
    def read_rds_table(self, db_connector, table_name):
        engine = db_connector.init_db_engine()
        user_data = pd.read_sql_table(table_name, engine, index_col='index')
        return user_data
```

  - PDF document in an AWS S3 bucket

```python
    def retrieve_pdf_data(self, link):
        pdf = tabula.convert_into(link, "pdf_output.csv", output_format="csv", pages='all')
        df = pd.read_csv('pdf_output.csv')
        pdf_df = pd.DataFrame(df)
        return pdf_df
```

  - API with API key

```python
    def retrieve_stores_data(self, retrieve_stores_endpoint, header_dict):
        stores_data_list = []
        for i in range(451):
            response = requests.get(retrieve_stores_endpoint + str(i), headers=header_dict)
            stores_data = response.json()
            df = pd.DataFrame(stores_data, index=[i])
            stores_data_list.append(df)
            stores_df = pd.concat(stores_data_list, ignore_index=True)
        return stores_df
```

  - CSV file in an AWS S3 bucket

```python
    def extract_from_s3(self, s3_url):
        s3_client = boto3.client('s3')
        product_df = pd.read_csv(s3_url)
        return product_df
```

- Once the data was cleaned, it was uploaded and stored in the new database 'sales_data'.

## Milestone 3

- Developed the star-based schema of the 'sales_data' database, ensuring all columns were the correct data types.

## Milestone 4

- Using SQL the business queries below could be answered;
  - How many stores does the business have and in which countries?
  - Which locations currently have the most stores?
  - Which months produce the highest cost of sales typically?
  - How many sales are coming from online?
  - What percentage of sales come through each type of store?
  - Which month in each year produced the highest cost of sales?
  - What is our staff headcount?
  - Which German store type is selling the most?
  - How quickly is the company making sales?

SQL query example:

```SQL
WITH cte AS
(SELECT TO_TIMESTAMP(CONCAT(year, '-', month, '-', day, ' ', timestamp), 'YYYY-MM-DD HH24:MI:SS') AS full_date_time,
year FROM dim_date_times
ORDER BY full_date_time DESC),
cte2 AS
(SELECT year, full_date_time, 
LEAD(full_date_time, 1) OVER (ORDER BY full_date_time DESC) AS time_difference FROM cte)
SELECT year, AVG((full_date_time - time_difference)) AS actual_time_taken FROM cte2
GROUP BY year
ORDER BY actual_time_taken DESC
LIMIT 5
```
