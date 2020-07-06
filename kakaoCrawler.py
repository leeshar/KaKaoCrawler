import simplejson,requests
import sys
import json
url = "https://dapi.kakao.com/v2/local/search/category.json?"
apikey = "6663b13431da132c67c66562c3465c30"
query = "카페"
page = 1
while(page < 46):
    r = requests.get( url, params = {'category_group_code': 'CE7' ,'category_group_name':query, 'page': page}, headers={'Authorization' : 'KakaoAK ' + apikey } )
    js = simplejson.JSONEncoder().encode(r.json())
    r.json()
    jstring = json.dumps(r.json(), indent=4, ensure_ascii=False)
    f = open('./kakao/data/kakaoCE7_'+str(page)+'.json', 'w', encoding="utf-8")
    f.write(jstring)
    f.close()
    print(r.json())
    page += 1