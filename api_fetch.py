import requests
import json

url = "https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open('cat_fact.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("資料抓取並儲存成功！")
else:
    print("抓取失敗，狀態碼：", response.status_code)
