from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions
from selenium.common.exceptions import WebDriverException, ElementClickInterceptedException, TimeoutException, StaleElementReferenceException, NoSuchElementException, NoSuchAttributeException
from configs import PathsConfig
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_site(url) -> dict[str, object]:
    options = FirefoxOptions()
    options.set_preference('media.volume_scale', 0) # выключаем звук
    # отключает всплывающие окна
    options.set_preference("dom.disable_open_during_load", True)
    # устанавливает макс кол-во всплывающих окон 0
    options.set_preference("dom.popup_maximum", 0)
    # отключает сообщения о блокировке всплывающих окон в браузере Firefox
    options.set_preference("privacy.popups.showBrowserMessage", False)
    
    
    # указываем юзер агента
    options.set_preference('general.useragent.override', 
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0')
    
    service = Service(
        executable_path=PathsConfig.DRIVER_PATH
    )
    browser = webdriver.Firefox(options=options, service=service)
    try:
        browser.maximize_window()
        browser.get(url)
        browser.implicitly_wait(10)
        src = browser.page_source
    except WebDriverException as ex:
        browser.close()
        browser.quit()
        raise WebDriverException('Ошибка октрытия сайта')
    result: dict = {
        'browser': browser,
        'src': src
    }

    return result







def click_next_page(browser: webdriver.Firefox) -> None:
    while True:
        """Разобраться с кнопкой клика"""
        wait = WebDriverWait(browser, 10)
        browser.implicitly_wait(10)
        try:
            btn = browser.find_element(By.CSS_SELECTOR, 'a[title="next page"].DDVsUa')
            btn.click()
            # src = browser.page_source
            # return src
        except StaleElementReferenceException as ex:
            print('', ex)
            # browser.refresh()
            btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="next page"].DDVsUa')))
            # нажимаем на кнопку ок банера
            try:
                btn.click()
                browser.implicitly_wait(10)
            except ElementClickInterceptedException  as ex:
                print('', ex)
                try:
                    banner_btn = wait.until(EC.element_to_be_clickable((By.ID, 'uc-btn-accept-banner')))
                    browser.execute_script("arguments[0].scrollIntoView(true);", banner_btn)
                    banner_btn.click()
                    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="next page"].DDVsUa')))
                    btn.click()
                    browser.implicitly_wait(10)
                    # src = browser.page_source
                    # return src
                except WebDriverException as ex:
                    print(ex)
                    browser.close()
                    browser.quit()
                    raise WebDriverException('Ошибка при переходе на следующую страницу')
                except TimeoutException:
                    pass
            except TimeoutException:
                pass
        except ElementClickInterceptedException  as ex:
            print('', ex)
            try:
                banner_btn = wait.until(EC.element_to_be_clickable((By.ID, 'uc-btn-accept-banner')))
                browser.execute_script("arguments[0].scrollIntoView(true);", banner_btn)
                banner_btn.click()
                btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="next page"].DDVsUa')))
                btn.click()
                browser.implicitly_wait(10)
                # src = browser.page_source
                # return src
            except WebDriverException as ex:
                print(ex)
                browser.close()
                browser.quit()
                raise WebDriverException('Ошибка при переходе на следующую страницу')
            except TimeoutException:
                pass
        except TimeoutException:
            pass
        return