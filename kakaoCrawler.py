import simplejson
import requests
import sys
import json
url = "https://dapi.kakao.com/v2/local/search/category.json?"
apikey = "6663b13431da132c67c66562c3465c30"
query = "카페"
number = 1
x = 125
y = 33.1
while(x < 131.87):
    if(38.4 < y):
        y = 33.1
        x += 0.15
    r = requests.get(url, params={'category_group_code': 'CE7', 'category_group_name': query,
                                  'x': x, 'y': y}, headers={'Authorization': 'KakaoAK ' + apikey})
    js = simplejson.JSONEncoder().encode(r.json())
    r.json()
    jstring = json.dumps(r.json(), indent=4, ensure_ascii=False)
    f = open('./data/kakaoCE7_' +
             str(number)+'.json', 'w', encoding="utf-8")
    f.write(jstring)
    f.close()
    print(r.json())
    y += 0.15
    number += 1
