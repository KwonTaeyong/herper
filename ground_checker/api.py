from urllib.parse import urlencode, unquote, quote_plus
import requests
import pprint
import json
import pandas as pd
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup

url = "http://apis.data.go.kr/6260000/BusanSoilCntmnInfoService/getSoilCntmnInfo?serviceKey=%2Bfo84XFieu%2FnOkCYp0ku9ORNXRG9cKPr9afezuVj6dFL4edX%2BqxcoehVvEaL3RL5Nv62XjcUaz4NinkqD4AJNg%3D%3D&pageNo=1&numOfRows=10&inspec_yy=2006&resultType=json"
response = requests.get(url)
contents = response.text
json_ob = json.loads(contents)
body = json_ob['getSoilCntmnInfo']['item']
dataframe = pd.json_normalize(body)



serviceKey = "%2Bfo84XFieu%2FnOkCYp0ku9ORNXRG9cKPr9afezuVj6dFL4edX%2BqxcoehVvEaL3RL5Nv62XjcUaz4NinkqD4AJNg%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def check_ground():
    station = []
    pm10 = []
    url = "http://apis.data.go.kr/6260000/BusanSoilCntmnInfoService/getSoilCntmnInfo?serviceKey=%2Bfo84XFieu%2FnOkCYp0ku9ORNXRG9cKPr9afezuVj6dFL4edX%2BqxcoehVvEaL3RL5Nv62XjcUaz4NinkqD4AJNg%3D%3D&pageNo=1&numOfRows=10&inspec_yy=2006&resultType=json"
    pageNo = "1"
    numOfRows = "10"
    inspec_yy = "2006"
    resultType = "json"

    queryParams = '?' + urlencode({quote_plus('ServiceKey'): serviceKeyDecoded,
                                   quote_plus('numOfRows'): numOfRows, quote_plus('pageNo'): pageNo,
                                   quote_plus('inspec_yy'): inspec_yy, quote_plus('resultType'): resultType})
    res = requests.get(url + queryParams, allow_redirects=False)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    for tag in soup.find_all('stationname'):
        station.append(tag.text)
    for tag in soup.find_all('pm10value'):
        pm10.append(tag.text)
    res = dict(zip(station, pm10))
    return res
