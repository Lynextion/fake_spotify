import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def you(url):
    global driver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,3)
    presence =EC.presence_of_element_located
    visible = EC.visibility_of_element_located

    driver.get("https://www.youtube.com/results?search_query="+url)

    
    return driver