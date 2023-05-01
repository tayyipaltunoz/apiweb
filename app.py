from flask import Flask, request, render_template
import requests
# import pandas as pd
# import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def search_api():
    if request.method == 'POST':
        # Kullanıcının girdiği değeri alalım
        query = request.form['query']

        # REST API'ye istek gönderelim
        response = requests.get('https://fakestoreapi.com/products/' + query)

        # API yanıtını bir değişkene ata
        try:
            result = response.json()

            # Sonucu bir Flask şablonunda kullanmak için değişkeni geri döndür
            return render_template('index.html', result=result)
        except Exception as ex:
            print(f'Sonuç bulunamadı. {ex}')
            error = (f'"{query}" için sonuç bulunamadı. {ex}')
            return render_template('index.html', error=error)

        # GET istekleri için basit bir HTML formu döndürelim

    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5001, debug=True)


# git config --global user.email "tayyip.altunoz@hotmail.com"
#   git config --global user.name "tayyipaltunoz"