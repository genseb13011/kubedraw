import sqlite3

def create_db(dbname):
  sqlite3.connect(dbname)