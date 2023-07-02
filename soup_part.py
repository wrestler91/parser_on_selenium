from bs4 import BeautifulSoup
import re 
from utils import get_model_info, get_price

def get_items(soup: BeautifulSoup) -> dict[str, dict[str, str]]:
    elements = soup.find_all('a', class_='q84f1m')
    
    data: dict = {}
    for element in elements:
        try:
            model_info = get_model_info(element)
            name = model_info['name']
            url = model_info['url']
        except Exception:
            print('Ошибка при парсинге ссылки или названия')
            name = 'no_data'
            url = 'no_data'

        try:
            price_info = get_price(element)
            price = price_info['price']
            discount = price_info['discount']
            valute = price_info['valute']
        except Exception:
            price = 'no_data'
            discount = 'no_data'
            valute = 'no_data'
            print('Ошибка при парсинге цены')
        print(name)
        data[name] = {
            'type': model_info['type'],
            'color': model_info['color'],
            'price': price,
            'valute': valute,
            'discount': discount,
            'url': url,
        }

    return data

    
def get_max_page(soup: BeautifulSoup) -> int:
    patern = re.compile(r'Page 1 of (\d+)')
    try:
        element = soup.find(string=patern)
        page = element.text[-1]
        return int(page)
    except Exception as ex:
        print('Не нашел число страниц')
        return 1



