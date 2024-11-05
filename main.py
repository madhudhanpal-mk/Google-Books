from flask import Flask, request, render_template
import requests


app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form['title']
        url = f'https://www.googleapis.com/books/v1/volumes?q={title}'
        response = requests.get(url).json()

        my_data = [
            {
                'book_title': response['items'][0]['volumeInfo']['title'],
                'price' : response['items'][1]['saleInfo']['listPrice']['amount'],
            }
        ]
        return render_template('index.html',my_data=my_data)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)