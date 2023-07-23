import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# seta as configuracoes do browser e inicia o webdriver selenium
def init_webdriver():
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })
    # Stop Selenium from closing browser automatically
    option.add_experimental_option("detach", True)
    # chromedriver should be in the same folder as file
    browser = webdriver.Edge(f'C:\webdrivers\Edge\msedgedriver.exe')
    return browser

# navega para a home do YT e navega para o video login
def login(browser, url):
    browser.get(url)
    browser.maximize_window()
    time.sleep(2)
    

def scroll_down(browser,locator,wait_time=2):
        "Scroll down"
        try:
            element = browser.find_element(By.ID, 'primary')
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(wait_time)
        except Exception as e:
            print(str(e),'debug')
            return None 


def core(url):
    browser = init_webdriver()
    login(browser, url)
    
    time.sleep(10)
    
    html = browser.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    
    time.sleep(2)
    comments = browser.find_elements(By.ID, "comment")

    
    # captura informacoes
    comments_data = list()
    # d_comment = dict.fromkeys(["author", "date", "text", "likes"])



    while comments != '' and comments != None:
        d_comment = dict.fromkeys(["author", "date", "text", "likes"])
        for items in comments:
            try:
                comment = items.text
                comment = comment.split('\n')
                d_comment["author"] = comment[0]
                d_comment["date"] = comment[1]
                d_comment["text"] = comment[2]
                d_comment["likes"] = comment[3]
                comments_data.append(d_comment)

                with open('./resources/comments_data.json', 'w', encoding='utf-8') as file:
                    file.write(json.dumps(comments_data, ensure_ascii=False).encode('utf-8').decode())
            except:
                pass
        html = browser.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        time.sleep(2)
        comments = browser.find_elements(By.ID, "comment")

    with open('./resources/comments_data.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(comments_data, ensure_ascii=False).encode('utf-8').decode())
