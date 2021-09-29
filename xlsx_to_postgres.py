import pandas as pd
from sqlalchemy import create_engine
import psycopg2
engine=create_engine("postgresql+psycopg2://postgres:backend2020@localhost:5432/Teste")
with pd.ExcelFile('Contratos.xlsx') as xls:
    df=pd.read_excel(xls)
    df.to_sql(name='contratos', con=engine, if_exists='append', index=False)
