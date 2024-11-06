from flask import Flask, request, render_template
import requests, json

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form['title']
        url = f'https://www.googleapis.com/books/v1/volumes?q={title}'
        response = requests.get(url).json()

        data = response['items']

        s1 = json.dumps(data)
        books = json.loads(s1)

        Mydb = []

        for i in range(len(data)):
            if 'listPrice' in books[i]['saleInfo']:
                tempBooks = {
                    'title': books[i]['volumeInfo']['title'],
                    'price' :books[i]['saleInfo']['listPrice']['amount'],
                    'currencyCode' :  books[i]['saleInfo']['listPrice']['currencyCode'],
                    'authors' : books[i]['volumeInfo']['authors']
                }
                print
                Mydb.append(tempBooks)
            else:
                tempBooks = {
                    'title' : books[i]['volumeInfo']['title'],
                    'price' : "Not for Sale",
                    'currencyCode' :  'Not Available',
                    'authors' : books[i]['volumeInfo']['authors']
                }
                Mydb.append(tempBooks)

        return render_template('index.html', Mydb = Mydb)
    
    #return render_template('index.html', Mydb = {'None': 'None'})
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
    