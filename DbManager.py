
import sqlite3

class DbManager:
    def __init__(self):
        pass

    def init_table(self):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        CREATE TABLE users (
            login VARCHAR(20) PRIMARY KEY ,
            password VARCHAR(20)
        );
        """
        cursor.execute(request)
        connection.close()

    def registration(self, login, password):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = f'INSERT INTO users (login, password) VALUES ("{login}","{password}");'
        cursor.execute(request)
        connection.commit()
        connection.close()

    def read_table(self, login):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        SELECT login, password FROM users WHERE login=?;
        """
        cursor.execute(request, (login,))
        R = cursor.fetchone()
        #RR = cursor.fetchall()
        connection.close()
        return R


    def delete(self, login):
        raise Exception("Error!")
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """DELETE FROM users WHERE login=?;"""
        
        cursor.execute(request, (login,))
        connection.close()

    def read_all_table(self):
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        request = """
        SELECT * FROM users ;
        """
        cursor.execute(request)
        RR = cursor.fetchall()
        
        connection.close()
        return RR





