import json
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

number = 1
while(number < 3):
    with open('./data/kakaoCE7_'+str(number)+'.json') as json_file:
        json_data = json.load(json_file)

        for documents in json_data['documents']:
            context = ssl._create_unverified_context()
            html = urlopen(documents['place_url'], context=context)
            bsObject = BeautifulSoup(html, 'html.parser')
            print(bsObject)
    number += 1
