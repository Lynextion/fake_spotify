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
import time
import os
import re
import string
import shutil


class player():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,3)
        self.presence = EC.presence_of_element_located
        self.visible = EC.visibility_of_element_located
        self.music_title = []
        self.singer = []
        self.music_href = []
        self.img_url = []
        self.installed_music = []
        self.music_id = ""
        self.counter =0
        self.id ='a'

        self.current_dic = os.getcwd()
        self.music_file = os.path.join(self.current_dic,'')
        directory = 'musics'
        self.path = os.path.join(self.current_dic, directory)
        
        try:
            os.mkdir(path)
        except:
            print('ok')

        


    def download(self,url,music_title):
        
        self.yt = YouTube(url)
        self.stream = self.yt.streams.filter(only_audio=True).first()
        out_file = self.stream.download()
        time.sleep(0.8)
        music_place = out_file
        music_place = music_place.replace(self.music_file,'')
        re.sub('\ |\?|\.|\!|\/|\;|\:', '',music_title)
        
        os.rename(out_file,self.path+"\\"+music_title)
        

        return (self.path+"\\"+music_title)
        
        

                

    def chrome(self):
        time.sleep(0.8)
        self.music_title = []
        self.music_href = []
        self.bf = BeautifulSoup(self.driver.page_source,'lxml')     
          
        for section in self.bf.find_all('ytd-video-renderer', class_='style-scope ytd-item-section-renderer'):  
            try:
                title=section.find('h3', class_='title-and-badge style-scope ytd-video-renderer').text
                print(title)
                self.music_title.append(title)   
                sing = section.find('a', class_='yt-simple-endpoint style-scope yt-formatted-string').text
                print(sing)
                self.singer.append(sing) 
                href = section.find('a', class_='yt-simple-endpoint style-scope ytd-video-renderer', href=True)
                self.music_href.append(href['href']) 
                img = section.find('img')
                self.img_url.append(img.get('src'))  

            except AttributeError:
                continue

        return  self.music_title,self.music_href
                
        

    def music_choose(self,music,music_title):
        re.sub('\ |\?|\.|\!|\/|\;|\:', '',music_title)
        
        # try:

         #    self.img_data = requests.get(self.img_url[music_choice]).content  

          #   with open('image.jpg','wb') as f:
           #      f.write(img_data)
         #except:
          #   print("nah")
  
        

        self.musics = open('names.txt','r')

        find = 0
        lists = self.musics.readlines()
        for line in lists:
            print(line,music_title)
            if line == music_title:
                print(line,"mmmmmm",music_title)
                find = 1
                name= music_title.replace(self.music_file,'')
                return (self.path+'\\'+name)
                pass
                       

        if find == 0:
            
            self.musics.close()
            self.musics = open('names.txt','a')
            self.url = "https://www.youtube.com"+music
            print("url",self.url)
            self.driver.get(self.url)  
            print("Downloading please wait...")
            name = self.download(self.url,music_title)
            self.musics.write(music_title+'\n')
            self.musics.close()
            print("Download complete")

            return (name)
        find = 0
                

    def search(self,choice):
        self.url = 'https://www.youtube.com/results?search_query='+choice
        self.driver.get(self.url)
