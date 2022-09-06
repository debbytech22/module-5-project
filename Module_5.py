import pandas as pd
import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/demo_db",pool_recycle=-1)
db_engine = engine.connect()
print("engine created successfully")
df= pd.read_csv("new_waec.csv")
df.to_sql(name="waec_data",con=engine,if_exists="append",index = False)
print("successful")
