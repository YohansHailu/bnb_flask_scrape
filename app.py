from flask import Flask
from bs4 import BeautifulSoup
import os
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def ScrapeIt():

    url = "https://coinmarketcap.com/currencies/bullperks/"
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    divs_with_circulating_supply = soup.find_all('div', string="Circulating supply")
    grandparent = divs_with_circulating_supply[0].find_parent().find_parent()
    circulating_supply = grandparent.find('dd').text

    circulating_supply =  circulating_supply.replace(',', '').replace('BLP', '')


    divs_with_total_supply = soup.find_all('div', string="Total supply")
    grandparent = divs_with_total_supply[0].find_parent().find_parent()
    total_supply = grandparent.find('dd').text
    total_supply = total_supply.replace(',', '').replace('BLP', '')


    return f"Circulating Supply: {circulating_supply}, Total Supply: {total_supply}"

if __name__ == '__main__':
    # Read port number from environment variable or use default 5000
    port = int(os.environ.get('PORT_NUMBER', 5000))
    app.run(debug=True, port=port)
