import simplejson,requests
import sys
import json
url = "https://dapi.kakao.com/v2/local/search/category.json?"
apikey = "6663b13431da132c67c66562c3465c30"
query = "CE7"
page = 1
r = requests.get( url, params = {'category_group_code':query}, headers={'Authorization' : 'KakaoAK ' + apikey } )
js = simplejson.JSONEncoder().encode(r.json())
r.json()
jstring = json.dumps(r.json(), indent=4, ensure_ascii=False)
f = open('kakaoCE7_'+str(page)+'.json', 'w', encoding="utf-8")
f.write(jstring)
f.close()
print(r.json())