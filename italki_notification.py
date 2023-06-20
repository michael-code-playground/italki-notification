import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#wait until an element you want to access is loaded (prevent an exception from being raised)
def wait_until_element_loaded(method,location):
    element = ""
    while True:
        try:
            element = driver.find_element(method, location)
        except:
            pass
        if element!="":
            break
    return element

#open the browser
driver = webdriver.Firefox()

#put url to a profile
driver.get("")

#wait 1s
time.sleep(1)

#initial condition
no_spots = False

#check if there's an available spot, if not, close the browser
try:
    slot = driver.find_element(By.CSS_SELECTOR, ".jsx-213674858.small-schedule-cell-active.h-full.w-full")
    driver.execute_script("arguments[0].click();", slot)
    
except:
    print("No spots available this week")
    no_spots = True

#if there's a spot, open the console
if no_spots == False:
    key = input("Are we booking or not? ")
    
    #if any character is entered by a user, head to opening/login 
    if key!= None:
        button_book = driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/button")
        driver.execute_script("arguments[0].click();", button_book)
        login_button = ""
        
        while True:
            try:
                login_button = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div/div[2]/div/div/div/div/div[6]/div/span[2]")
            except:
                pass
            if login_button!="":
                break
        
        driver.execute_script("arguments[0].click();", login_button)
        
        #enter your credentials 
        input_mail = wait_until_element_loaded(By.ID,"signinForm_email")
        input_mail.send_keys("")

        input_pass = wait_until_element_loaded(By.ID,"signinForm_password")
        input_pass.send_keys("")
else:
    driver.quit()




                 
        