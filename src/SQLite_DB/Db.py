import sqlite3
import sys
sys.path.append(".")
from configs.config import DB_NAME

def singleton(cls, *args, **kw):
   instances = {}
   def _singleton(*args, **kw):
      if cls not in instances:
           instances[cls] = cls(*args, **kw)
      return instances[cls]
   return _singleton

@singleton
class DB_Sqlite3:
    def __init__(self):
        self.db_name = DB_NAME
        self.conn = sqlite3.connect("./src/SQLite_DB/"+DB_NAME+".db",check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns = ', '.join(columns)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert(self, table_name, columns, values):
        columns = ', '.join(columns)
        values = ', '.join([f"'{value}'" for value in values])
        print(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.conn.commit()

    #return a list
    def select_Table(self, table_name, columns):
        columns = ', '.join(columns)
        self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        return self.cursor.fetchall()

    def select_where(self, table_name, columns, condition):
        columns = ', '.join(columns)
        condition = ' and '.join(condition)
        print(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        return self.cursor.fetchall()

    def update(self, table_name, columns, values, condition):
        columns = ', '.join([f"{column} = '{value}'" for column, value in zip(columns, values)])
        self.cursor.execute(f"UPDATE {table_name} SET {columns} WHERE {condition}")
        self.conn.commit()
        
    def close(self):
        self.conn.close()
