import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm

df = pd.read_csv("kuda_data.csv", encoding="cp1252") ## using microsoft encoding instead of UTF-8 bcus of em dash in data 
df.head()
df.dtypes
df.shape

engine = create_engine('postgresql+psycopg://root:root@localhost:5432/kuda_data')
print(pd.io.sql.get_schema(df, name='kuda_loan_data', con=engine))

parse_dates = ["date"]
dtype = {
'customer_id': 'string'
,'loan_id': 'string'
,'loan_amount': 'Int64'
,'cumulative_repayment':'Int64'
,'cumulative_interest':'Int64'
,'cumulative_paid':'Int64'
,'outstanding_balance':'Int64'
,'days_in_arrears':'Int64'
,'status': 'string'
,'utilization (%)':'Float64'
,'DPD_bucket': 'string'
,'risk_band' : 'string'
}

df_iter = pd.read_csv('Kuda_data.csv', dtype=dtype, parse_dates=parse_dates, chunksize=500, encoding="cp1252")

first = True
for df_chunk in tqdm(df_iter):
    if first:
        df_chunk.head(n=0).to_sql(
            name='kuda_loan_data'
            , con=engine
            , if_exists='replace'
        )
        first = False
        print("Table Created")
        
    df_chunk.to_sql(
        name='kuda_loan_data'
        , con=engine
        , if_exists='append'
    )
    print(f"Inserted {len(df_chunk)} rows to Kuda_loan_data")
print("Table successfully created \n Data successfully ingested!")