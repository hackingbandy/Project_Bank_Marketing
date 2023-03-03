import pandas as pd
import main

## open csv file
bank = pd.read_csv("bank.csv")

## add table to database
bank.to_sql("bank", main.conn, if_exists="append", index=False)