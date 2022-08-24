from selenium import webdriver
import time
import xlsxwriter
import pandas as pd
import threading

parcels = ['paste in list of failures from browser_get.py to check why they are wrong']#update from browser_get.py failed queries
print(len(parcels))
browser = webdriver.Chrome("path to chromedriver.exe")#update
fails = []

for x in range(0, len(parcels)):
    try:
        browser.get("https://apps.montgomerycountymd.gov/realpropertytax/")
        browser.find_element_by_id("ctl00_MainContent_ParcelCode").send_keys(f"{parcels[x]}")
        browser.find_element_by_xpath('//*[@id="ctl00_MainContent_btnAcc"]').click()
        browser.find_element_by_xpath('//*[@class="btn btn-success btn-sm"]').click()                                            
        address = browser.find_element_by_id("ctl00_MainContent_lblCompleteAddress")
        name = browser.find_element_by_id("ctl00_MainContent_lblName")
        occupancy = browser.find_element_by_id("ctl00_MainContent_lblOccupancy")
        print(x, address.text.lstrip("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`~!@#$%^&*()_+-=,.//<>?;':{}[]\| "), occupancy.text, name.text)
        
    except:
        fails.append(parcels[x])

print(fails)

print(fails)       
#workbook.close()
browser.close()
