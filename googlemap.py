from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep 

driver = webdriver.Chrome("C:\Program Files (x86)/chromedriver") 
driver.get("https://www.google.com/maps/@19.1540166,76.2113025,14z") 
sleep(2) 

def searchplace():
	   Place=driver.find_element_by_class_name("tactile-searchbox-input")
	   Place.send_keys("Pune")
	   Submit=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
	   Submit.click()
searchplace()

def directions():
	   sleep(10)	
	   directions=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span/img")
	   directions.click()
directions()

def find():
         sleep(6)
         find=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
         find.send_keys("Aurangabad")
         sleep(2)
         search=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
         search.click()
find()

# def kilometers():
#                sleep(5)
#                Totalkilometers=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[2]/div")
#                print("Total Kilometers:",Totalkilometers.text)
#                sleep(5)
#                Bus=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[1]/div[1]/div[1]/span[1]")
#                print("Bus Travel:",Bus.text)
#                sleep(7)
#                Train=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div")
#                print("Train Travel:",Train.text)
#                sleep(7)

# kilometers()
while(True):
    pass
