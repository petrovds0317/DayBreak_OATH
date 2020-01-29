
import sqlite3
import datetime
import time
import random

class Dbproxy:
    def __init__(self):
        self.db = DbManager()

    def get_password(self, login):
        p = self.db.read_table(login)
        if p:
            return p[1]
        else:
            return None

    def write_ticket(self, login, ticket, time):
        self.db.registration_tickets(login, ticket, time)

    def get_login(self, ticket):
        login = self.db.read_table_tickets(ticket)
        time = self.db.example_time(ticket)
        print("login =", login)
        print("Time= ", time)
        if login:
            if time != None:
                return login[0]
        else:
            return None

    def get_ticket(self, login):
        ticket = self.db.return_ticket(login)
        if ticket:
            return ticket[0]
        else:
            None

    def new_ticket(self, a, new_ticket):
        login = a["login"]
        old_ticket = self.db.return_ticket(login)       
        self.db.delete_tickets(old_ticket[0])
        time = self.db.read_time(old_ticket)
        return self.db.registration_tickets(login, new_ticket, time )
    
        #c = self.db.registration_tickets( login, ticket, time)
        #return b, c


    def ticket_number(self):   
        rand = random.randrange(10000, 100001, 1)
        return str(rand)
    

class DbManager:
    def __init__(self):
        pass
        
    def connect(self): 
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        return connection, cursor
    
    def read_all_table(self):
        conn, cur = self.connect()

        request = """
        SELECT * FROM users ;
        """
        cur.execute(request)
        result = cur.fetchall()
        
        conn.close()
        return result

    def init_table(self):
        conn, cur = self.connect()
        request = """
        CREATE TABLE users (
            login VARCHAR(20) PRIMARY KEY ,
            password VARCHAR(20)
        );
        """
        cur.execute(request)
        conn.close()

    def init_table_tickets(self):
        conn, cur = self.connect()
        request = """
        CREATE TABLE tickets (
            login VARCHAR(20) PRIMARY KEY ,
            ticket VARCHAR(20), time INTEGER(20)
        );
        """
        cur.execute(request)
        conn.close()

    def registration(self, login, password):
        conn, cur = self.connect()

        request = f'INSERT INTO users (login, password) VALUES ("{login}","{password}");'
        cur.execute(request)
        conn.commit()
        conn.close()

    def registration_tickets(self, login, ticket, time):
        conn, cur = self.connect()
        request = f'INSERT INTO tickets (login, ticket, time) VALUES ("{login}","{ticket}","{time}");'
        cur.execute(request)
        conn.commit()
        conn.close()

    def example_login(self, ticket):
        conn, cur = self.connect()

        request = """
        SELECT login FROM tickets WHERE ticket=?;
        """
        cur.execute(request, (ticket,))
        result = cur.fetchone()
        conn.close()
        return result
    
    
    def read_table(self, login):
        conn, cur = self.connect()

        request = """
        SELECT login, password FROM users WHERE login=?;
        """
        cur.execute(request, (login,))
        R = cur.fetchone()
        conn.close()
        return R

    def read_table_tickets(self, ticket):
        conn, cur = self.connect()
        request = """
        SELECT login FROM tickets WHERE ticket=?;
        """
        cur.execute(request, (ticket,))
        R = cur.fetchone()
        conn.close()
        return R

    


    def delete(self, login):
        conn, cur = self.connect()
        request = """DELETE FROM users WHERE login=?;"""
        
        cur.execute(request, (login,))
        conn.commit()
        conn.close()

    def delete_tickets(self, ticket):
        conn, cur = self.connect()
        request = """DELETE FROM tickets WHERE ticket=?;"""
        
        cur.execute(request, (ticket,))
        conn.commit()
        conn.close()

    

    def read_all_table_tickets(self):
        conn, cur = self.connect()
        request = """
        SELECT * FROM tickets ;
        """
        cur.execute(request)
        RR = cur.fetchall()
        
        conn.close()
        return RR

    def read_time(self, ticket):
        conn, cur = self.connect()
        request = """
        SELECT time FROM tickets WHERE ticket=?;
        """
        cur.execute(request, (ticket,))
        R = cur.fetchone()
        conn.close()
        return R

    def example_time(self, ticket):       
        now = time.time() 
        a = int(now)
        print("now", a)
        b = self.read_time(ticket)
        bb = b[0]
        print("ticket", bb)

        if a < bb:
            return bb
        else:
            return None

    def return_ticket(self, login):
        conn, cur = self.connect()
        request = """
        SELECT ticket FROM tickets WHERE login=?;
        """
        cur.execute(request, (login,))
        R = cur.fetchone()
        conn.close()
        return R



a = DbManager()
b = DbManager()
a = Dbproxy()
b = Dbproxy()

#a.init_table()
#a.init_table_tickets()

#a.registration("admin","1111")
#a.registration_tickets("admin","5555",1579999380)
#a.delete_tickets("tic-aaa")

#print(a.example_login("tic-ccc"))


#print(a.read_table("admin"))
#print(a.read_table_tickets("tic-ccc"))

#print(a.read_all_table())
#print(a.read_all_table_tickets())


#print(a.read_time("tic-cc1"))
#print(b.get_login("tic-vvv"))

#print(a.example_time("tic-vvv"))
#print(datetime.datetime.now())

#print(b.random_number())

#print(a.return_ticket("admin"))
#print(b.get_ticket("admin"))
ss = {'login' : 'log-vvv', 'password' : 'tic-vvv'}
print(b.new_ticket( ss , "00000"))

#print(a.read_all_table_tickets())
