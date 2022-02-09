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

@app.route("/allvbaprojects/")
def CW_AllVBAProjects():    # get all of VBA projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    GetWebElement(driver, ElementType.Class, "search_freeword", 10).find_element_by_tag_name("input").send_keys("VBA")      # 検索テキストボックスを取得、VBAと入力
    GetWebElement(driver, ElementType.Class, "cw-input_group_button", 10).find_element_by_tag_name("button").click()  # 検索ボタンを押す
    eachAnkenName = GetALlAnkenName(driver)
    return render_template('index.html', data=zip(eachAnkenName))

@app.route("/allpythonprojects/")
def CW_AllPythonProjects():     # get all of Python projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    GetWebElement(driver, ElementType.Class, "search_freeword", 10).find_element_by_tag_name("input").send_keys("Python")      # 検索テキストボックスを取得、VBAと入力
    GetWebElement(driver, ElementType.Class, "cw-input_group_button", 10).find_element_by_tag_name("button").click()  # 検索ボタンを押す
    eachAnkenName = GetALlAnkenName(driver)
    return render_template('index.html', data=zip(eachAnkenName))

@app.route("/allapiprojects/")
def CW_AllAPIProjects():        # get all of API projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    GetWebElement(driver, ElementType.Class, "search_freeword", 10).find_element_by_tag_name("input").send_keys("API")      # 検索テキストボックスを取得、VBAと入力
    GetWebElement(driver, ElementType.Class, "cw-input_group_button", 10).find_element_by_tag_name("button").click()  # 検索ボタンを押す
    eachAnkenName = GetALlAnkenName(driver)
    return render_template('index.html', data=zip(eachAnkenName))

# Init Chrome instance and go to CrowdWorks
def InitCrowdworks():
    driver = webdriver.Chrome()
    driver.get("https://crowdworks.jp/public/jobs?category=jobs&order=score&ref=toppage_hedder")
    return driver

# get WebElement
def GetWebElement(driver, elementType, elementName, timeout):
    now = InitTime()    # Init time instance
    nowTime = int(now.strftime('%Y%m%d%H%M%S'))      # get now time
    untilTime = nowTime + timeout       # calc timeout
    # loop until nowtime gets larger than timeout
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
        nowTime = int(now.strftime('%Y%m%d%H%M%S'))  # get now time
    return webElement

# get WebElements
def GetWebElements(driver, elementType, elementName, timeout):
    now = InitTime()    # Init time instance
    nowTime = int(now.strftime('%Y%m%d%H%M%S'))      # get now time
    untilTime = nowTime + timeout       # calc timeout
    # loop until nowtime gets larger than timeout
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
        nowTime = int(now.strftime('%Y%m%d%H%M%S'))  # get now time
    return webElements

# Init time instance
def InitTime():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    return now

# get all of project's name
def GetALlAnkenName(driver):
    webElements = GetWebElements(driver, ElementType.Class, "item_title", 10)
    eachAnkenName = []
    for eachElement in webElements:
        eachAnkenName.append(eachElement.text)
    return eachAnkenName