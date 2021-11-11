#importing thimgs needed

from selenium import webdriver
import pyautogui
import time

#initialization

driver = webdriver.Chrome("C:/Users/rajaa/Desktop/projects/AVYT/chromedriver_updated.exe")
driver.get('https://www.google.com')
driver.maximize_window()
time.sleep(3)
pyautogui.click(x=281, y=68)
pyautogui.write('https://www.youtube.com/shorts/7RHHLPJwSN4')
time.sleep(2)
pyautogui.press('enter')


i=0
for i in range(10):
    if i==10:
        break
    else:
        i=i+1
        time.sleep(35)
        pyautogui.click(x = 107, y = 63)
