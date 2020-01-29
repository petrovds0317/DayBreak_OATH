from flask import Flask, render_template, request
import json

app=Flask(__name__)

@app.route('/entry', methods=['GET','POST'])
def auth():
    a=request.get_json()
    if a == None:
        return "Wrong Data"
    k=a.keys()
    if "login" in k and "password" in k:
        return "None"
    else:
        answer={}
        answer["Error"]="2"
        answer["Message"]="Не введен логин или пароль"
        print(json.dumps(answer))
        return json.dumps(answer)

#именно команда return отправляет json, причем текст в консоле будет показан в виде байт символов, а не нормальных букв










'''
    return render_template('entry_m.html', the_title='Welcome!')
'''

if __name__=='__main__':
    app.run(debug=True)


    
