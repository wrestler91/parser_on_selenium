from bs4 import BeautifulSoup
import json
import csv
from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from configs import SiteInfoConfig
from selenium_part import open_site, click_next_page
from soup_part import get_items, get_max_page
from utils import upload_to_json, upload_to_CSV


# test_url = 'C:/Users/Арутюн/Desktop/python/проекты/scraper_and_parser/parser_with_selenium/testing_sample.html'

def main():
    data: dict = {}
    for brand in SiteInfoConfig.brands:
        for gender in SiteInfoConfig.genders:
            url = SiteInfoConfig.domain+SiteInfoConfig.sub_url+gender+brand
            data_start = open_site(url)
            browser = data_start['browser']
            src = data_start['src']
            soup = BeautifulSoup(src, 'lxml')
            max_page: int = get_max_page(soup)
            brnd = brand.strip('/')
            temp = {}
            temp[gender] = {}
            data[brnd] = temp
            for page in range(max_page):
                items: dict = get_items(soup)
                data[brnd][gender].update(items)
                if page < max_page-1:
                    src = click_next_page(browser)
                    src = browser.page_source
                soup = BeautifulSoup(src, 'lxml')
            

    upload_to_json(path='data/data_from_zolando.json', data=data)
    upload_to_CSV(path='data/data_from_zolando.csv', data=data)


                
    browser.close()
    browser.quit()
if __name__ == '__main__':
    main()

            
