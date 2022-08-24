from selenium import webdriver
import time
import xlsxwriter
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('path to xlsx output', engine='openpyxl') #update
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['Group', 'Parcel', 'District','Name', 'FCV', 'Amount Due'])
# Print the content
parcels = []
for x in range(0, len(data)):
    parcels.append(str(data['Parcel'][x]).zfill(8))
print(len(parcels))

workbook = xlsxwriter.Workbook('path to xlsx output') #update
browser = webdriver.Chrome("path to chromedriver.exe") #update
worksheet = workbook.add_worksheet()
fails = []
fail_line = []
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
        worksheet.write(f'A{x+1}', address.text.lstrip("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`~!@#$%^&*()_+-=,.//<>?;':{}[]\| "))
        worksheet.write(f'B{x+1}', occupancy.text)
        worksheet.write(f'C{x+1}', name.text)
    except:
        fails.append(parcels[x])
        fail_line.append(x)

print(fails)
print(fail_line)
workbook.close()
browser.close()

