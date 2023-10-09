from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import random
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.chrome.options import Options 
 
username = "inkyasaikyou"
password = "Kamekiti1192"
 
searchWord = "love"

 
 
# ログイン
def login(driver):
    # Instagram ログインページへ移動
    loginUrl = "https://www.instagram.com/"
    driver.get(loginUrl)
    driver.implicitly_wait(30)
 
    # Usernameを入力
    usernameInput = driver.find_element(By.CSS_SELECTOR, "input[name=username]")
    usernameInput.send_keys(username)
    sleep(3)
 
    # Passwordを入力
    passwordInput = driver.find_element(By.CSS_SELECTOR, "input[name=password]")
    passwordInput.send_keys(password)
    sleep(3)
    # ログインをクリック
    loginButton = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
    loginButton.click()
    
    return driver
    
 
# urlが投稿ページかどうかを確認
def is_post_url(url):
    if "/p/" in url:
        return True
    else:
        return False
 
    
def is_liked(soup):
    if soup.find("svg", {"aria-label": "「いいね！」を取り消す"}) is None:
        return True
    else:
        return False
    
# SeleniumでChromeを起動
service = Service(executable_path='C:\\Users\\tikua\\programs\\instagram\\instagram\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)
 
# ログイン
driver = login(driver)
 
time.sleep(5)  # 5秒間待つ

"""
定期的に実行する際には、ログインした状態を維持したまま、これより下のコードを繰り返した方がいいです。
毎回ログインしてるとすぐに怪しまれます。
"""
 
# tagページへ移動
tagUrl = "https://www.instagram.com/explore/tags/{}/?hl=ja"
driver.get(tagUrl.format(searchWord))   
driver.implicitly_wait(30)

time.sleep(5)  # 5秒間待つ
 
# aタグを取得
urlList = [item.get_attribute("href") for item in driver.find_elements(By.TAG_NAME, "a")]

 
# 各投稿へアクセスしていいね！を押す
for url in urlList:
    if is_post_url(url):
        print(url)
        driver.get(url)
        driver.implicitly_wait(30)
        sleep(3)
 
        # htmlの取得
        soup = BeautifulSoup(driver.page_source, "html.parser")
 
        # いいね！が押されていなかったら押す
        if is_liked(soup):
            like_button_selector = "div.x1i10hfl.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.x78zum5.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.xcdnw81 svg[aria-label='いいね！']"
            element = driver.find_element(By.CSS_SELECTOR, like_button_selector)
            element.click()
 
        # 数秒待機
        waitTime = random.choice(range(1, 6))
        print("{}秒待機...".format(waitTime))
        sleep(waitTime)