from flask import Flask, request,render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_api():
    if request.method == 'POST':
        # Kullanıcının girdiği değeri alalım
        query = request.form['query']
        
        # REST API'ye istek gönderelim
        response = requests.get('https://fakestoreapi.com/products/' + query)
        
        # API'den gelen cevabı döndürelim
        return response.content       
    
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


