from   flask     import Flask, request
import requests
import random
import json
from utilities import *


# Генерация тикета
ticket_number = round(random.random()*10000)

app=Flask(__name__)

### ПРОВЕРКА ЛОГИНА И ПАРОЛЯ

# Получение запроса от клиента и отправка тикета далее или сообщение об ошибке
@app.route("/auth", methods=["GET"])
def auth():
    a = request.get_json()
    if validate(a) == True:
        if check(a) == True:
            return str(ticket_number)
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
    app.run(port=5002)



# у нас нет страниц сейчас, мы разговариваем с сервером, есть ответы серверы
#именно команда return отправляет json, причем текст в консоле будет показан в виде байт символов, а не нормальных букв

# в браузере может выводится сообщение сервера, но сам браузер нам не посылает пока никаких данных


