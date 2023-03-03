import sqlite3
from pathlib import Path

##create empty database
Path("bank.db").touch()

##connect db
conn = sqlite3.connect("bank.db")
c = conn.cursor()
print(conn)
print(c)

##create table if not exist (default => default_e)
c.execute(
    """CREATE TABLE IF NOT EXISTS bank(
    age int,
    job varchar(255),
    marital varchar(255),
    education varchar(255),
    default_e text, 
    balance int,
    housing text,
    loan text
    contact text,
    day int,
    month text,
    duration int,
    campaign int,
    pdays text,
    previous int,
    poutcome text,
    deposit text
    );
    """
)
