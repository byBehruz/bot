import requests

from data.config import BASE_URL

import json
def all_info(telegram_id):
    response = requests.post(f'{BASE_URL}/ru/my_app/bot-users', data={
    'telegram_id':telegram_id})
    data = json.loads(response.text)
    return data
    #####language#####
def language_info(telegram_id):
    response = requests.post(f"{BASE_URL}/ru/my_app/user", data={'telegram_id':telegram_id})
    data = json.loads(response.text)
    return data['language']

    #######categories#####
def get_categories(language):
    response = requests.get(f'{BASE_URL}/ru/my_app/category')
    data = json.loads(response.text)
    categories = [i['name'] for i in data]
    return categories
    ########rus and uzb######
def get_all_categories():
    response = requests.get(f'{BASE_URL}/ru/my_app/product')
    data = json.loads(response.text)
    category_uz = [i['description_uz'] for i in data]
    category_ru = [i['description_ru'] for i in data]
    return category_ru+category_uz
#     ########  search category#####
# def category_info(language,category):
#     response = requests.get(f'{BASE_URL}/{language}/api/category/?search={category}')
#     data = json.loads(response.text)
#     data = data[0]
#     if data[]
     #########get product#######
def get_product(id, language):
    response = requests.get(f'{BASE_URL}/{language}/my_app/product/{id}/')
    data = json.loads(response.text)
    return data
    ######### create user######
def create(name, telegram_id):
    response = requests.post(f'{BASE_URL}/ru/my_app/bot-users', data={'name':name,'telegram_id':telegram_id})
    return response.status_code
    ######change language#####
def change_language(telegram_id, language):
    response = requests.post(f'{BASE_URL}/ru/my_app/language', data={'telegram_id':telegram_id, 'language':language})
    return response.status_code
    ######change phone#####
# def change_phone(telegram_id, phone):
#     response = requests.post(f'{BASE_URL}/phone/', data={'telegram_id':telegram_id, 'phone':phone})
#     return response.status_code
