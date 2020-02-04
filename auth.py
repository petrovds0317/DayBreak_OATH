from flask import Flask, request, render_template
import requests
import random
import json
from utilities import validate, check, make_error_message, validate_ticket, check_ticket, make_error_message_ticket
from DbManager import Dbproxy, DbManager


# Генерация тикета
#ticket_number = round(random.random()*10000)

db_manager = Dbproxy()
app = Flask(__name__)

### ПРОВЕРКА ЛОГИНА И ПАРОЛЯ

# Получение запроса от клиента и отправка тикета далее или сообщение об ошибке
@app.route("/auth", methods=["GET"])
def auth():
    a = request.get_json()
    if validate(a) == True:
        if check(a) == True:
            new_ticket = db_manager.ticket_number()                         
            return 
            
        else:
            return make_error_message("1")
    else:
        return make_error_message("2")


#### ПРОВЕРКА ЛОГИНА И ТИКЕТА ####################################################

# Получение запроса от клиента и отправка тикета далее или сообщение об ошибке
@app.route("/validate", methods=["GET"])
def take_ticket():
    t = request.get_json()
    if validate_ticket(t) == True:
        if check_ticket(t) == True:
            return str("Идет ссесия для данного тикета")
        else:
            return make_error_message_ticket("1")
    else:
        return make_error_message_ticket("2")

if __name__=='__main__':
    app.run(port=5002, host = "0.0.0.0" )



# у нас нет страниц сейчас, мы разговариваем с сервером, есть ответы серверы
#именно команда return отправляет json, причем текст в консоле будет показан в виде байт символов, а не нормальных букв

# в браузере может выводится сообщение сервера, но сам браузер нам не посылает пока никаких данных


