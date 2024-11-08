import sqlite3

class DB_Sqlite3:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect("./SQLite_DB/"+self.db_name,check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns = ', '.join(columns)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert(self, table_name, columns, values):
        columns = ', '.join(columns)
        values = ', '.join([f"'{value}'" for value in values])
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.conn.commit()

    def select_Table(self, table_name, columns):
        columns = ', '.join(columns)
        self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

