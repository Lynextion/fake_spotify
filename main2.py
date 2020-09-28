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
from pytube import YouTube



class player():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.wait = WebDriverWait(driver,3)
        self.presence = EC.presence_of_element_located
        self.visible = EC.visibility_of_element_located
        self.music_title = []
        self.singer = []
        self.music_href = []
        self.img_url = []


    def download(self,url):
        self.yt = YouTube(url)
        self.stream = yt.streams.filter(only_audio=True).first()
        self.stream.download()
        self.url
        self.bf

    def chrome(self)
        while True:
                
            self.search(    
            for section in bf.find_all('div', class_='style-scope ytd-video-renderer')  
                try:
                    title=section.find('h3', class_='title-and-badge style-scope ytd-video-renderer').text
                    print(title)
                    self.music_title.append(title   
                    sing = section.find('a', class_='yt-simple-endpoint style-scope yt-formatted-string').text
                    print(sing)
                    self.singer.append(sing 
                    href = section.find('a', class_='yt-simple-endpoint style-scope ytd-video-renderer', href=True)
                    self.music_href.append(href['href'] 
                    img = section.find('img')
                    self.img_url.append(img.get('src')  
                except AttributeError:
                    continue
                
           

    def music_choose(self):

        music_choice = int(input('Please enter num for choose:'))
        try:

            self.img_data = requests.get(self.img_url[music_choice]).content  

            with open('image.jpg','wb') as f:
                f.write(img_data)
        except:
            continue

        self.url = "https://www.youtube.com"+self.music_href[music_choice] 
        self.driver.get(url)  
        print("Downloading please wait...")
        self.download(url)
        print("Download complete")


    def search(self,choice):
        self.url = 'https://www.youtube.com/results?search_query='+choice
        self.driver.get(url)
        self.bf = BeautifulSoup(driver.page_source,'lxml')
