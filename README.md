# Multinational Retail Centralisation

Scenario: You work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team. In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location. Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data. You will then query the database to get up-to-date metrics for the business.

## Milestone 1

- Set up of the dev environment.

## Milestone 2

- Extracted and cleaned the data from multiple data sources;
  - AWS database
  - PDF document in an AWS S3 bucket
  - API with API key
  - CSV file in an AWS S3 bucket
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