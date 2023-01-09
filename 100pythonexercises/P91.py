#CSV to database

import sqlite3
import pandas

data = pandas.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database.db")
curr = conn.cursor()
for index,row in data.iterrows():
    print(row["country"],row["Area"])
    curr.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["country"],row["Area"]))
conn.commit()
conn.close()
