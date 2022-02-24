import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.youtube.com/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

wait = WebDriverWait(browser, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

video = "Pop Smoke Dior"

browser.get('https://www.youtube.com/results?search_query={}'.format(str(video)))

wait.until(visible((By.ID, "video-title")))
browser.find_element_by_id("video-title").click()




