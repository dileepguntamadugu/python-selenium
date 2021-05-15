import pytest
import pytest_html
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestRegisterNewInstructor(unittest.TestCase):

    def main(self):
        testaddtocart(self)

    def testaddtocart(self):
        jsclickscript = 'arguments[0].click();'
        #Try using headless mode once you get comfortable
        #options = Options()
        #options.add_argument('--headless')
        #options.add_argument('--disable-gpu')
        #driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.mooseknucklescanada.com/")
        print(driver.current_url)
        driver.maximize_window()
        title = driver.title
        print("title is: "+title)
        waitcss(driver,"#eshopworld-landing-page > div > div > form > fieldset > div.field.actions-toolbar > div > button > span")
        continueshopping = driver.find_element_by_css_selector('#eshopworld-landing-page > div > div > form > fieldset > div.field.actions-toolbar > div > button > span')
        continueshopping.click()
        waitcss(driver,"#maincontent > div.columns > div > div:nth-child(3) > div > div.home-main-banner > div > div > div > div > div > div.headerContentWrapper.can-store-hp-inline > div > div:nth-child(2) > a")
        women = driver.find_element_by_css_selector("#maincontent > div.columns > div > div:nth-child(3) > div > div.home-main-banner > div > div > div > div > div > div.headerContentWrapper.can-store-hp-inline > div > div:nth-child(2) > a")
        driver.implicitly_wait(2)
        driver.execute_script(jsclickscript,women)
        #women.click()
        waitcss(driver, "[alt='Pegboy Shorts M11LR757 Knockout Pink Front']")
        pinkshorts = driver.find_element_by_css_selector("[alt='Pegboy Shorts M11LR757 Knockout Pink Front']")
        pinkshorts.click()
        waitcss(driver, "[option-label='Knockout Pink']")
        color = driver.find_element_by_css_selector("[option-label='Knockout Pink']")
        color.click()
        waitcss(driver, "[option-label='M']")
        mediumsize = driver.find_element_by_css_selector("[option-label='M']")
        mediumsize.click()
        waitcss(driver, "#product-addtocart-button")
        addtocart = driver.find_element_by_css_selector("#product-addtocart-button")
        addtocart.click()
        proceedtocheckout = driver.find_element_by_css_selector('#maincontent > div.columns > div > div.cart-container > div > ul > li > button')
        waitcss(driver, '#maincontent > div.columns > div > div.cart-container > div > ul > li > button')
        proceedtocheckout.click()
        print('>>>>>>>>>>>Hey Sweetie!!!!!!!!!!!!!!!!! Now you continue developing the remaining solutions')
        print(driver.current_url)
        assert 'https://www.mooseknucklescanada.com/en/checkout/' == driver.current_url()
        driver.close()

def waitcss(driver, cssselector):
    WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, cssselector))
            )

def waitxpath(driver, xpath):
    WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

if __name__ == "__main__":
    main()