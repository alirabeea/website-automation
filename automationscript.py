import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
import PySimpleGUI as sg
from decouple import config

video = ""

sg.theme("Black")

layout = [  [sg.Text('Enter name of video'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('WebAuto', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or video != "":
        break
    video = values[0];

window.close()

url = 'https://www.youtube.com/'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

wait = WebDriverWait(browser, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

browser.get('https://www.youtube.com/results?search_query={}'.format(str(video)))

wait.until(visible((By.ID, "video-title")))
browser.find_element(By.ID,"video-title").click()

sleep(6)

try:
    wait.until(visible((By.CLASS_NAME, "ytp-ad-skip-button")))
    browser.find_element(By.CLASS_NAME, "ytp-ad-skip-button").click()
except:
    print("no ad")

try:
    wait.until(visible((By.ID, "dismiss-button")))
    browser.find_element(By.ID, "dismiss-button").click()
except:
    print("no dismiss")

SAVE_PATH = config("SAVE_PATH")

yt = YouTube(browser.current_url)

yt = yt.streams.get_highest_resolution()

try:
    yt.download(SAVE_PATH)
    sg.popup('Downloaded video successfully.')
    
except:
    sg.popup('Download failed.')


sleep(10)

open(SAVE_PATH)
sg.close()
browser.close()