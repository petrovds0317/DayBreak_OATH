import requests

url = "http://127.0.0.1:5000/entry"
data = {"login": "<имя>", "password": "<пароль>"}
message = requests.post(url, json=data)

# отправляем в интернет наш словарь json

# во втором терминале тоже запускать этот файл

print(message.text)
