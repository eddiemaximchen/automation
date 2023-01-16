'''
匯入套件
'''
# 操作 browser 的 API
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
# 處理逾時例外的工具
from selenium.common.exceptions import TimeoutException
# 面對動態網頁，等待某個元素出現的工具，通常與 exptected_conditions 搭配
from selenium.webdriver.support.ui import WebDriverWait
# 搭配 WebDriverWait 使用，對元素狀態的一種期待條件，若條件發生，則等待結束，往下一行執行
from selenium.webdriver.support import expected_conditions as EC
# 期待元素出現要透過什麼方式指定，通常與 EC、WebDriverWait 一起使用
from selenium.webdriver.common.by import By
# 強制等待 (執行期間休息一下)
from time import sleep
# 整理 json 使用的工具
import json
# 執行 command 的時候用的
import os
'''
selenium 啓動 Chrome 的進階配置參數
參考網址：https://stackoverflow.max-everyday.com/2019/12/selenium-chrome-options/
'''
# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")         #最大化視窗
my_options.add_argument("--incognito")               #開啟無痕模式
my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  #設定為正體中文
# 使用 Chrome 的 WebDriver
my_service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(
    options = my_options,
    service = my_service
)
# 開啟網頁
driver.get("https://www.104.com.tw/jobs/main/")
# 尋找網頁中的搜尋框
inputElement = driver.find_element(By.CSS_SELECTOR, 'input#ikeyword')
# 在搜尋框中輸入文字
inputElement.send_keys("python")
# 睡個幾秒
sleep(2)
# 按鈕選擇器
cssSelectorBtn = "button.btn.btn-primary.js-formCheck"
try:
    # 等待元素
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, cssSelectorBtn)
        )
    )   
    # 取得按鈕元素
    btn = driver.find_element(By.CSS_SELECTOR, cssSelectorBtn)    
    # 按下按鈕
    btn.click()   
    # 睡個幾秒
    sleep(3)
except TimeoutException:
    print('等待逾時！')
# 開啟網頁
driver.get("https://reurl.cc/jR725D")
# 睡個幾秒
sleep(5)
# 刷新頁面
driver.refresh()
# 睡個幾秒
sleep(5)
# 刷新頁面
driver.refresh()
# 關閉瀏覽器
driver.quit()