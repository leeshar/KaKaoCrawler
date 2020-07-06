import json
number = 1
while(number < 3):
    with open('./data/kakaoCE7_'+str(number)+'.json') as json_file:
        json_data = json.load(json_file)

        for documents in json_data['documents']:
            print(documents['place_url'])
    number += 1
