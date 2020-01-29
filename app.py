#ЭТО КЛИЕНТ

# Из внешнего источника (например, телефона клиента) получаем данные
j = {"login": "admin", "password":"1111"}
l = {"login": "admin", "ticket":"5555"}

# для дебаггинга послали данные на сервер и получили ответ
import requests
url1 = "http://127.0.0.1:5002/auth"
r = requests.get(url=url1, json=j)

url2 = "http://127.0.0.1:5002/validate"
s = requests.get(url=url2, json=l)

print(r.text)
print(s.text)