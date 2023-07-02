from bs4 import BeautifulSoup
import json
import csv

# def build_url(domain: str, sub_url: str, gender: str, brand: str):
#     return 


def get_price(data: BeautifulSoup) -> dict:
    info = data.find('section').find_all('p')
    if len(info) == 2:
        discount = info[1].find_all('span')[-1].text.strip('up to ')

    else:
        discount = 0
    price_info = info[0].find_all('span')
    if len(price_info) == 2:
        price_text = price_info[1].text
    elif len(price_info) == 1:
        price_text = price_info[0].text

    price_data = price_text.split()
    price, valute = price_data
    return {
        'discount': discount,
        'price': price,
        'valute': valute,
    }
    

def get_model_info(data: BeautifulSoup) -> dict:

    if data.find('div', class_='Zhr-fS'):
        item_name = data.find_all('h3')
        if item_name:
            url = data.get('href')
            brand, model_data = item_name[0].text, item_name[1].text
            model_info = model_data.split(" - ")
            if len(model_info) == 3:
                model, type_, color = model_info
            else:
                model, type_, color = model_data, 'no_data', 'no_data'
            name = f'{brand} {model}'
            res = {
                'url': url,
                'name': name,
                'type': type_,
                'color': color,
            }
            return res
    raise ValueError('Ошибка при поиске имени товара')


def upload_to_json(path: str, data: dict)-> None:
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def upload_to_CSV(path: str, data: dict) -> None:
    result: list = []
    for brand, gender_data in data.items():
        for gender, model_data in gender_data.items():
            for model, detail_data in model_data.items():
                values = detail_data.values()
                temp = [model, *values, gender, brand]
                result.append(temp)

    with open(path, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(result)


def upload_page(path: str, src: str) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        file.write(src)

def read_local_page(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as file:
        src = file.read()
    return src