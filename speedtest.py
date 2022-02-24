
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui as pya
driver = webdriver.Chrome('sciezka do googledrive')
driver.get('https://10fastfingers.com/typing-test/english')
time.sleep(2)
cookie = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[4]/div[1]/div[2]/button[4]').click()
time.sleep(1)
while True:
    slowko = driver.find_element(By.CSS_SELECTOR,'#row1 > span.highlight').text
    wpisz = driver.find_element(By.XPATH,'/html/body/div[5]/div/div[4]/div/div[1]/div[7]/div[2]/div/div[1]/input')
    wpisz.send_keys(slowko)
    pya.press('space')
            
