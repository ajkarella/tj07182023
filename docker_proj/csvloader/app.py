import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')

# load apple data
df = pd.read_csv('data/appleAppData.csv')
df.to_sql('apple_data', engine, index=False, if_exists='replace')

# load android data
df = pd.read_csv('data/Google-Playstore.csv')

# replace spaces with underscores so it's easier to work with in db
cols = df.columns
new_cols = []
for i in cols:
    new_cols.append(i.replace(" ","_"))
df.columns = new_cols

df.to_sql('android_data', engine, index=False, if_exists='replace')