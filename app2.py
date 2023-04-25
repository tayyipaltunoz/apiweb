from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        # REST API'ye sorgu gönderme
        response = requests.get('https://fakestoreapi.com/products/' + input_text)
        # API'den gelen cevabı alıp kullanıcı arayüzünde gösterme
        result = response.json()
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)