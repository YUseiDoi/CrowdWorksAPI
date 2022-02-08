from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from enum import Enum
import datetime

app = Flask(__name__)

# Type of WebElement
class ElementType(Enum):
    ID = 0
    Class = 1
    Name = 2
    Tag = 3
    PartialLinkText = 4
    Label = 5
    Linktext = 6
    Xpath = 7
    Unknown = -1

@app.route("/allproject/")
# Main
def CrowdWorksAPIMain():
    driver = InitCrowdworks()       # Chromeインスタンスを初期化し、CrowdWorksにアクセス
    #webElement = GetWebElement(driver, ElementType.Class, "cw-form_control", 10)        # 検索テキストボックスを取得
    #webElement.send_keys("VBA")     # VBAと入力
    #GetWebElement(driver, ElementType.Class, "cw-input_group_button", 10).find_element_by_tag_name("button").click()  # 検索ボタンを押す
    eachAnkenName = GetALlAnkenName(driver)
    return render_template('index.html', data=zip(eachAnkenName))

# Chromeインスタンスを生成し、CrowdWorksサイトにアクセスする
def InitCrowdworks():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get("https://crowdworks.jp/public/jobs?category=jobs&order=score&ref=toppage_hedder")
    return driver

# WebElementを取得
def GetWebElement(driver, elementType, elementName, timeout):
    now = InitTime()    # 時刻を初期化
    nowTime = int(now.strftime('%Y%m%d%H%M%S'))      # 現在時刻を取得
    untilTime = nowTime + timeout       # タイムアウト時刻を計算
    # 現在時刻がタイムアウト時刻を越えるまでループ
    while nowTime < untilTime:
        if elementType == ElementType.ID:
            webElement = driver.find_element_by_id(elementName)
        elif elementType == ElementType.Class:
            webElement = driver.find_element_by_class_name(elementName)
        elif elementType == ElementType.Name:
            webElement = driver.find_element_by_name(elementName)
        elif elementType == ElementType.Tag:
            webElement = driver.find_element_by_tag_name(elementName)
        elif elementType == ElementType.PartialLinkText:
            webElement = driver.find_element_by_partial_link_text(elementName)
        elif elementType == ElementType.Xpath:
            webElement = driver.find_element_by_xpath(elementName)
        elif elementType == ElementType.Linktext:
            webElement = driver.find_element_by_link_text(elementName)
        else:
            print("予期せぬエラーが発生しました")
        if webElement != None:
            break
        nowTime = int(now.strftime('%Y%m%d%H%M%S'))  # 現在時刻を取得
    return webElement

# WebElementを取得
def GetWebElements(driver, elementType, elementName, timeout):
    now = InitTime()    # 時刻を初期化
    nowTime = int(now.strftime('%Y%m%d%H%M%S'))      # 現在時刻を取得
    untilTime = nowTime + timeout       # タイムアウト時刻を計算
    # 現在時刻がタイムアウト時刻を越えるまでループ
    while nowTime < untilTime:
        if elementType == ElementType.ID:
            webElements = driver.find_elements_by_id(elementName)
        elif elementType == ElementType.Class:
            webElements = driver.find_elements_by_class_name(elementName)
        elif elementType == ElementType.Name:
            webElements = driver.find_elements_by_name(elementName)
        elif elementType == ElementType.Tag:
            webElements = driver.find_elements_by_tag_name(elementName)
        elif elementType == ElementType.PartialLinkText:
            webElements = driver.find_elements_by_partial_link_text(elementName)
        elif elementType == ElementType.Xpath:
            webElements = driver.find_elements_by_xpath(elementName)
        elif elementType == ElementType.Linktext:
            webElements = driver.find_elements_by_link_text(elementName)
        else:
            print("予期せぬエラーが発生しました")
        if webElements != None:
            break
        nowTime = int(now.strftime('%Y%m%d%H%M%S'))  # 現在時刻を取得
    return webElements

# 時刻インスタンスを初期化
def InitTime():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    return now

# 案件タイトルを全て取得
def GetALlAnkenName(driver):
    webElements = GetWebElements(driver, ElementType.Class, "item_title", 10)
    eachAnkenName = []
    for eachElement in webElements:
        eachAnkenName.append(eachElement.text)
    return eachAnkenName