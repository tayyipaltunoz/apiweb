from flask import Flask, request,render_template
import requests
import pandas as pd
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_api():
    if request.method == 'POST':
        # Kullanıcının girdiği değeri alalım
        query = request.form['query']
        
        # REST API'ye istek gönderelim
        response = requests.get('https://fakestoreapi.com/products/' + query)
        
        # API yanıtını bir değişkene ata
        result = response.json()  
        
        # with open('response.json','w') as f:
        #     json.dump(result, f)
        
        # with open('response.json') as f:
        #     data = pd.read_json(f)

        # # DataFrame'i HTML formatına dönüştür
        # html_table = data.to_html()

        # # with open('')
        # # HTML tablosunu görüntüle
        # print(html_table)
        
        # result = html_table
        
        # Sonucu bir Flask şablonunda kullanmak için değişkeni geri döndür
        return render_template('index.html', result=result)
   
    
    # GET istekleri için basit bir HTML formu döndürelim
    
    return render_template("index.html")
    # return '''
    #     <form method="post">
    #         <input type="text" name="query" placeholder="Aranacak değer...">
    #         <input type="submit" value="Ara">
    #     </form>
    # '''


if __name__ == '__main__':
    app.run(port=5001,debug=True)


