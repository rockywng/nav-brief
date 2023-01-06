from flask import Flask, request
import scraper.scraper as sc

app = Flask(__name__)

@app.route('/', methods=['GET'])
def search_api():
    scraper = sc.Scraper()
    query = request.args.get('code')
    return scraper.findSpeci(query)

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
