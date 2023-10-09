from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
import random
from selenium.webdriver.common.by import By 
import time
from instagrapi import Client

cl = Client()
 
username = "inkyasaikyou"
password = "Kamekiti1192"

try:
    cl.login(username, password)  # instagrapiを使用してログイン
    print("Login successful")
except Exception as e:
    print(f"Login failed: {e}")
    exit()
 
 
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

try:
    # 'love'のハッシュタグに関連する最近の投稿を取得
    medias = cl.hashtag_medias_recent_v1('love', amount=20)
    base_url = "https://www.instagram.com/p/"
    
    url_list = []  # URLを保存するための空のリストを作成
    
    # 取得した投稿の詳細を辞書形式で出力
    for media in medias:
        # 投稿のコード（code）を出力
        code = media.dict().get('code')
        full_url = base_url + code  # base_urlをcodeに付け加える
        url_list.append(full_url)  # 完全なURLをリストに追加
        # print(full_url)  # 完全なURLを出力
        
except Exception as e:
    print(f"Error: {e}")
 
time.sleep(5)  # 5秒間待つ 
 
# url_list内の各URLにアクセスしていいねを押す
for url in url_list:
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