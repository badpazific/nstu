from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

login = 'naumenko.2018@stud.nstu.ru'
password = 'Rfgbnfy1'

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("http://nstu.ru")
time.sleep(2)

bnt_login = driver.find_element_by_css_selector("div.header__login>a")

bnt_login.click()

time.sleep(1)
bnt_kabinet = driver.find_element_by_xpath('//a[text() = "Кабинет обучающегося"]')
bnt_kabinet.click()

time.sleep(6)

input_login = driver.find_element_by_name('callback_0')
input_password = driver.find_element_by_name('callback_1')

input_login.send_keys(login)
input_password.send_keys(password)
input_password.send_keys(Keys.RETURN)

time.sleep(2)

bnt_title = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/table[4]/tbody/tr/td[3]/a/div")
bnt_title.click()
time.sleep(2)

bnt_title = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[4]/table[2]/tbody/tr/td[3]/a/div")
bnt_title.click()

time.sleep(2)

r = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/table[1]/tbody/tr")
rc = len(r)
a =""
for i in range(2, rc + 1):
 d = driver.find_element_by_xpath("/html/body/div[2]/div[2]/table[1]/tbody/tr["+str(i)+"]/td[2]").text
 a = a + "   " + d

print(a)

import json

dictionary = {"Список дисциплин:" : a}

jsontext = json.dumps(dictionary)

with open("List", "w") as f:
    f.write(jsontext)
    
time.sleep(5)