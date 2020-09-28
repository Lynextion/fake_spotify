from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.amazon.com/s?k=headphones&ref=nb_sb_noss_2'

driver = webdriver.Chrome()
wait = WebDriverWait(driver,3)
presence =EC.presence_of_element_located
visible = EC.visibility_of_element_located

driver.get(url)

bf = BeautifulSoup(driver.page_source,'lxml')

products=[]
orginal_price=[]
prices=[]





for search in bf.find_all('div', class_ ='a-section a-spacing-medium'):
    result = search.find('a', class_='a-link-normal a-text-normal').text
    print(result)
    products.append(result)
    f.write(result)

    
    try:
        
        price = search.find('span', class_='a-offscreen').text
        print("Orjinal fiyatı",price)
        orginal_price.append(price)
        f.write(price)
    
    except AttributeError:
        print("değeri yok")


for kar in orginal_price:
    add = kar * 10
    add = int(add) / 100
    prices.append(kar+add)
    print(kar)
    