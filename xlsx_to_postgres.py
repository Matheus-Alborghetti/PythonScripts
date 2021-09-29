import pandas as pd
from sqlalchemy import create_engine
import psycopg2
engine=create_engine("postgresql+psycopg2://user:password@localhost:5432/dbname")
with pd.ExcelFile('file.xlsx') as xls:
    df=pd.read_excel(xls)
    df.to_sql(name='name', con=engine, if_exists='append', index=False)
