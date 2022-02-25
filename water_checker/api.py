from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup

serviceKey = "%2Bfo84XFieu%2FnOkCYp0ku9ORNXRG9cKPr9afezuVj6dFL4edX%2BqxcoehVvEaL3RL5Nv62XjcUaz4NinkqD4AJNg%3D%3D"
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def check_water():
    station = []
    pm10 = []
    url = "http://www.dgwater.go.kr:8080/openapi-data/service/rest/InqireWaterQualityInfoSrvc/getWaterQualityStatisticsInfo?serviceKey=%2Bfo84XFieu%2FnOkCYp0ku9ORNXRG9cKPr9afezuVj6dFL4edX%2BqxcoehVvEaL3RL5Nv62XjcUaz4NinkqD4AJNg%3D%3D&year=2014"
    year = '2014'

    queryParams = '?' + urlencode({quote_plus('ServiceKey'): serviceKeyDecoded, quote_plus('year'): year})
    res = requests.get(url + queryParams, allow_redirects=False)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    for tag in soup.find_all('stationname'):
        station.append(tag.text)
    for tag in soup.find_all('pm10value'):
        pm10.append(tag.text)
    res = dict(zip(station, pm10))
    return res
