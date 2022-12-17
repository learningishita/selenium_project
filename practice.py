from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

optn = webdriver.ChromeOptions()
optn.add_argument('headless')
driver = webdriver.Chrome("C:/Users/Ashish Goyal/Downloads/chromedriver_win32/chromedriver.exe",options=optn)
main_url = "https://indianhelpline.com/"
driver.get(main_url)
v = driver.find_elements(By.ID,'wb_element_instance1163')
for i in v:
    state_name = str(i.text)
state_name = state_name.split('\n')
header = ['StateName', 'Type', 'Phone Number']
f = open('C:/Users/Ashish Goyal/Desktop/devOps_challenges/prog2.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)
# print(state_name)
# for j in "ANDAMAN AND NICOBAR ISLAND":

v = driver.find_element(By.LINK_TEXT,"ANDAMAN AND NICOBAR ISLAND")
url = str(v.get_attribute("href"))
print(url)
driver.get(url)
print("Site Opened")
detail_info = driver.find_elements(By.CLASS_NAME,"wb-stl-special")
Name_Type=[]
Phone_Number=[]
all_info = []
count = 0
for k in detail_info:
    k = str(k.text)
    all_info.insert(count,k)
    count = count +1
iterations = 0
print(len(all_info))
print(all_info)
for i in range(len(all_info)-1):
    if(all_info[iterations].isdigit()):
        Phone_Number.append(all_info[iterations])
        iterations+=1
    else:
        Name_Type.append(all_info[iterations])
        iterations+=1
print("Name of the type")
print(Name_Type)
print("Phone_Number")
print(Phone_Number)
#     print(len(detail_info))
#     i = str(i.text)
#     if i == "© 2015 - 2022 Indianhelpline.com":
#         break
#     else:
#         f = open('C:/Users/Ashish Goyal/Desktop/devOps_challenges/prog2.csv', 'w')
#         writer = csv.writer(f)
#         for m in range(len(detail_info)-1):
            
#             writer.writerow([j,])
#             driver.get(main_url)
        # try:
        #     print(i.text)
        # except NoSuchElementException as exception:
        #     exit
# writer.writerow(value)
# print("came out of loop")
# data = pd.read_csv("prog2.csv")
# data = pd.DataFrame(data)
# for i in range(1):
#         i = str(data.loc[i,'StateName'])
#         v = driver.find_element(By.LINK_TEXT,i)
#         url = str(v.get_attribute("href"))
#         optn = webdriver.ChromeOptions()
#         optn.add_argument('headless')
#         driver = webdriver.Chrome("C:/Users/Ashish Goyal/Downloads/chromedriver_win32/chromedriver.exe",options=optn)
#         driver.get(url)
#         detail_info = driver.find_element(By.CLASS_NAME,"wb-stl-special")
#         print(detail_info.size)