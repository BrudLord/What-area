import sys
from io import BytesIO
from find_spn_param import find_spn
import requests
from PIL import Image, ImageDraw, ImageFont
import math

# Пусть наше приложение предполагает запуск:
# python main.py Москва, улица Тимура Фрунзе, 11к8
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = input()

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
# Долгота и широта:
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": ','.join(toponym_coodrinates.split(" ")),
    'kind': 'district',
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
json_response = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
json_response = json_response['metaDataProperty']['GeocoderMetaData']['Address']['Components']
for i in json_response:
    if i['kind'] == 'district':
        print(i['name'])