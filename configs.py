from dataclasses import dataclass

@dataclass
class SiteInfoConfig:
    domain: str = "https://en.zalando.de"
    genders: tuple[str] = ('women', 'men',)
    # genders: tuple[str] = ('women',)
    sub_url: str = "/sports-shoes-"
    # brands: list[str] = ['/puma/', '/nike/', '/adidas/']
    brands: list[str] = ('/puma/', '/adidas/',)

@dataclass
class PathsConfig:
    DRIVER_PATH: str = 'C:/Users/Арутюн/Desktop/python/проекты/scraper_and_parser/geckodriver.exe'

# site_info = {
#     'doman': "https://en.zalando.de",
#     'genders': ('women', 'men'),
#     'sub_url': "/sports-shoes-",
#     'brands': ['/puma/', '/nike/', '/adidas/'],
# }

