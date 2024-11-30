#Practical : 24-  To study about the selenium library. 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('http://google.com')
browser.implicitly_wait(5)
search_elem = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
search_elem.send_keys("AMTICS")
search_btn = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
browser.implicitly_wait(1)
search_btn.click()
x = browser.find_element(By.XPATH, "/html/body/div[7]/div/div[11]/div[2]/div[3]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[1]/a")
x.click()

browser.get("https://accounts.google.com")
e_mail = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
e_mail.send_keys("bendalejatin35@gmail.com")
next = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()

