import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.idus.com/v2/category/1056'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
movieInfoList = soup.findAll('div', {'class': 'BaseProductCardVertical BaseProductCardVertical__size--large'})

def extract_price(price_str):
    # '원'을 제거하고 숫자만 남기는 정규 표현식 사용
    price_number = int(''.join(filter(str.isdigit, price_str)))
    return price_number
movie_data = []

for movieInfo in movieInfoList:

    Img = movieInfo.find('img')
    Nick = movieInfo.find('span', {'class': 'line-clamp-1 gray-999--text cursor-pointer'})
    title = movieInfo.find('div', {'class': 'BaseProductCardVertical__productName'})
    price = movieInfo.find('div', {'class': 'text-ellipsis'})
    price = extract_price(price.get_text().strip()) if price else "X"

    movie_data.append({
        'image': Img['src'] if Img else "X",
        'nick': Nick.get_text().strip() if Nick else "X",
        'price': price,
        'title': title.get_text().strip() if title else "X",
    })

# Convert the movie data to JSON
json_data = json.dumps(movie_data, ensure_ascii=False, indent=4)
print(json_data)
#
server_url = 'http://localhost:8111/api/goods/insert'
headers = {"Content-Type": "application/json; charset=utf-8"}
response = requests.post(server_url, data=json_data.encode('utf-8'), headers=headers)  # You need to encode the data

print("Data sent to the server successfully!")