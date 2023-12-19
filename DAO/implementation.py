import mysql.connector as sql

class DbConnection:
    def open(self):
        try:
            self.conn = sql.connect(host='localhost', database='casestudy', user='root', password='Ilovemymom@24')
            self.s = self.conn.cursor()
            print("Database is connected")
        except Exception as e:
            print(str(e) + "---Database is not Connected:--")

    def close(self):
        try:
            if self.conn.is_connected():
                self.s.close()
                self.conn.close()
                print('Connection Closed.')
        except Exception as e:
            print(str(e) + "---Error closing the connection.")


db_connection = DbConnection()
db_connection.open()
db_connection.close()
