import pandas as pd
import numpy as np
from airflow.decorators import task


# from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


def pandas_join_dataframes() -> pd.DataFrame:
    # Creating the customers dataframe
    data_data_customers = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    df_customers = pd.DataFrame(data_data_customers, columns=['id', 'name'])

    # Creating the orders dataframe
    data_orders = [[1, 3], [2, 1]]
    df_orders = pd.DataFrame(data_orders, columns=['id', 'customerId'])

    # merging the two dataframes
    df_merge_col = pd.merge(df_customers, df_orders, left_on='id', right_on='customerId', how='outer', indicator=True)

    print(df_merge_col.head())

    # creating the condition to discard the matching ones with the column _merge and value 'left_only'
    condition_df_merge = df_merge_col._merge == 'left_only'
    df_result = df_merge_col.loc[condition_df_merge, ['name']]

    print(df_result.head())

    # changing the column name 'name' to 'Customers'
    df_result_rename = df_result.rename(columns={'name': 'Customers'})

    print(df_result_rename.head())

# df_Customers, df_Orders = create_pandas_dataframes()
# pandas_join_dataframes(df_Customers,df_Orders)
