from src.settings import *


class Database:
    def __init__(self):
        self.my_db = mysql.connector.connect(
            host="localhost",
            user='root',
            password='root'
        )
        self.my_cursor = self.my_db.cursor()

    def use_database(self, name_database: str):
        self.my_cursor.execute(f"USE {name_database}")

    def insert_into_table(self, table_name, col_list, data_list):
        self.my_cursor.execute("USE my_discord")

        columns = ", ".join(f"{col}" for col in col_list)
        values = ", ".join(f"'{value}'" for value in data_list)
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        self.my_cursor.execute(query)
        self.my_db.commit()
        # self.close_all()

    def show_databases(self):
        self.my_cursor.execute("SHOW DATABASES")
        print("Databases:")
        for database in self.my_cursor:
            print(f"    - {database[0]}")

    def show_tables(self):
        self.my_cursor.execute("SHOW TABLES")
        print("Tables:")
        for table in self.my_cursor:
            print(f"    - {table[0]}")

    def open_file_sql(self):
        try:
            with open('sql/my_discord.sql') as f:
                sql = f.read()
            self.my_cursor.execute(sql)
        except mysql.connector.InterfaceError:
            pass

    def close_all(self):
        self.my_cursor.close()
        self.my_db.close()

    def create_my_discord(self):
        self.open_file_sql()
        self.close_all()

    def get_messages(self, column_name, id_channel):
        # print(column_name, id_channel)
        self.my_cursor.execute(f'SELECT {column_name} FROM messages WHERE id_channel = {id_channel}')
        results = self.my_cursor.fetchall()
        my_list = []

        for i in range(0, len(results)):
            my_list.append(results[i][0])

        # print(my_list)        
        return my_list
