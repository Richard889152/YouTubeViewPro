from selenium import webdriver       #YoutubeViewPro
from time import sleep

PewDiePie1= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")#In executable path give the path of chromedriver that you have downloaded. In my case it is in downloads.
PewDiePie2= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")
PewDiePie3= webdriver.Chrome(executable_path="C:\Users\siddh\Downloads\Compressed\chromedriver_win32\chromedriver")

PewDiePie1.get("https://youtu.be/429WCrxZqe0")#Channel PewDiePie
PewDiePie2.get("https://youtu.be/429WCrxZqe0")
PewDiePie3.get("https://youtu.be/429WCrxZqe0")
#i have used siddharth 1,2,3  so it will open 3 tabs 
#if you want to add more tabs you can also do it 

while True:
    sleep(18)#sleep 18 meanes after 18 seconds page will refresh
    PewDiePie1.refresh()
    PewDiePie2.refresh()
    PewDiePie3.refresh()
    
    #To execute - Simple run this code
    #By: xX Marcio Vinicius Xx