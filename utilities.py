from DbManager import Dbproxy
import json

db_manager = Dbproxy()

def validate(x):
    if x == None:
        return False
    k = x.keys() 
    if "login" in k and "password" in k:
        return True
    else:
        return False

def check(x):
    login = x["login"]
    password = x["password"]
    if password == db_manager.get_password(login):
        return True
    else:
        return False

messages = {"1":"Неправильные данные", "2":"Данные не введены"}
def make_error_message(code):
    d={}
    d["code"] = code
    d["message"] = messages[code]
    return json.dumps(d)

#################################################################3

def validate_ticket(y):
    if y == None:
        return False
    h = y.keys()
    if "login" in h and "ticket" in h:
        return True
    else:
        return False

def check_ticket(y):
    login = y["login"]
    ticket = y["ticket"]
    if login == db_manager.get_login(ticket) and ticket == db_manager.get_ticket(login):
        return True
    else:
        return False

messages2 = {"1":"Неправильные данные", "2":"Данные не введены"}
def make_error_message_ticket(code_ticket):
    d={}
    d["code"] = code_ticket
    d["message"] = messages2[code_ticket]
    return json.dumps(d)


#-----------------------------------------------------
#Проверка функции чек , validate
"""a = { "login" :"admin", "password" :"1111"}
b = check(a)
print(b)
#-----------------------------------------------------
c = validate(a)
print(c)"""