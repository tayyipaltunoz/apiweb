from flask import Flask, request, render_template,redirect,url_for
import requests
# import pandas as pd
# import json

app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route('/', methods=['GET', 'POST'])
def search_api():
    if request.method == 'POST':
        # Kullanıcının girdiği değeri alalım
        query = request.form['query'].upper()
        
        if query == "" :
            pass
        
        else :
            
            

            # REST API'ye istek gönderelim
            # response = requests.get('https://fakestoreapi.com/products/' + query)
            response = requests.get('https://dummyjson.com/products/' + query)
            
            # API yanıtını bir değişkene ata
            try:
                result = response.json()

                # Sonucu bir Flask şablonunda kullanmak için değişkeni geri döndür
                return render_template('index.html', result=result)
            except Exception as ex:
                print(f'Sonuç bulunamadı. {ex}')
                error = (f'"{query}" için sonuç bulunamadı. {ex}')
                return render_template('index.html', error=error)


    return render_template("index.html")

@app.route('/login')
def logout():
    return render_template('login.html')


@app.route('/login',methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "123456":
            return render_template('index.html')
        else:
            return render_template("login.html", error="Invalid username or password")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
    