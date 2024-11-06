from flask import Flask, request, render_template
import requests


app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form['title']
        url = f'https://www.googleapis.com/books/v1/volumes?q={title}'
        response = requests.get(url).json()

        data = {
            'total_books' : response['totalItems'],
            'book_title' :response['items'][0]['volumeInfo']['title'],
            #'price' : response['items'][0]['saleInfo']['listPrice']['amount']
        }
        return render_template('index.html',data=data)
    return render_template('index.html', data = {'None': 'None'})


if __name__ == "__main__":
    app.run(debug=True)
    