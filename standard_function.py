from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from enum import Enum
import datetime
from selenium.webdriver.support.select import Select
from flask import jsonify

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

# Selenium Class
class ChromeOperation:
    def __init__(self):
        option = Options()
        option.add_argument('--headless')
        #self.driver = webdriver.Chrome(options=option)  # chrome is not visible
        self.driver = webdriver.Chrome()         # chrome is visible
        self.driver.get("https://crowdworks.jp/public/jobs?category=jobs&order=score&ref=toppage_hedder")

    # get WebElement
    def GetWebElement(self, elementType, elementName, timeout):
        now = self.InitTime()  # Init time instance
        nowTime = int(now.strftime('%Y%m%d%H%M%S'))  # get now time
        untilTime = nowTime + timeout  # calc timeout
        # loop until nowtime gets larger than timeout
        while nowTime < untilTime:
            if elementType == ElementType.ID:
                webElement = self.driver.find_element_by_id(elementName)
            elif elementType == ElementType.Class:
                webElement = self.driver.find_element_by_class_name(elementName)
            elif elementType == ElementType.Name:
                webElement = self.driver.find_element_by_name(elementName)
            elif elementType == ElementType.Tag:
                webElement = self.driver.find_element_by_tag_name(elementName)
            elif elementType == ElementType.PartialLinkText:
                webElement = self.driver.find_element_by_partial_link_text(elementName)
            elif elementType == ElementType.Xpath:
                webElement = self.driver.find_element_by_xpath(elementName)
            elif elementType == ElementType.Linktext:
                webElement = self.driver.find_element_by_link_text(elementName)
            else:
                print("予期せぬエラーが発生しました")
            if webElement != None:
                break
            nowTime = int(now.strftime('%Y%m%d%H%M%S'))  # get now time
        return webElement

    # get WebElements
    def GetWebElements(self, elementType, elementName, timeout):
        now = self.InitTime()  # Init time instance
        nowTime = int(now.strftime('%Y%m%d%H%M%S'))  # get now time
        untilTime = nowTime + timeout  # calc timeout
        # loop until nowtime gets larger than timeout
        while nowTime < untilTime:
            if elementType == ElementType.ID:
                webElements = self.driver.find_elements_by_id(elementName)
            elif elementType == ElementType.Class:
                webElements = self.driver.find_elements_by_class_name(elementName)
            elif elementType == ElementType.Name:
                webElements = self.driver.find_elements_by_name(elementName)
            elif elementType == ElementType.Tag:
                webElements = self.driver.find_elements_by_tag_name(elementName)
            elif elementType == ElementType.PartialLinkText:
                webElements = self.driver.find_elements_by_partial_link_text(elementName)
            elif elementType == ElementType.Xpath:
                webElements = self.driver.find_elements_by_xpath(elementName)
            elif elementType == ElementType.Linktext:
                webElements = self.driver.find_elements_by_link_text(elementName)
            else:
                print("予期せぬエラーが発生しました")
            if webElements != None:
                break
            nowTime = int(now.strftime('%Y%m%d%H%M%S'))  # get now time
        return webElements

    # Init time instance
    def InitTime(self):
        t_delta = datetime.timedelta(hours=9)
        JST = datetime.timezone(t_delta, 'JST')
        now = datetime.datetime.now(JST)
        return now

    # get all of project's name
    def GetALlAnkenName(self):
        webElements = self.GetWebElements(ElementType.Class, "item_title", 10)
        eachAnkenName = []
        for eachElement in webElements:
            eachAnkenName.append(eachElement.text)
        return eachAnkenName

    # get all project's URL
    def GetAllAnkenURLs(self):
        webElements = self.GetWebElements(ElementType.Class, "item_title", 10)
        AllAnkenURL = []
        i = 0
        for i in range(len(webElements)):
            AllAnkenURL.append(webElements[i].find_element_by_tag_name("a").get_attribute("href"))
        return AllAnkenURL

    # keyword search
    def SearchKeyword(self, keyword):
        self.GetWebElement(ElementType.Class, "search_freeword", 10).find_element_by_tag_name("input").send_keys(
            keyword)  # 検索テキストボックスを取得、VBAと入力
        self.GetWebElement(ElementType.Class, "cw-input_group_button", 10).find_element_by_tag_name(
            "button").click()  # 検索ボタンを押す

    # get new projects'name
    def GetNewProjectsInformation(self):
        myDataOperation = DataOperation()           # create new instance of DataOperation
        Select(self.GetWebElement(ElementType.Class, "cw-form_group", 10).find_element_by_tag_name(
            "select")).select_by_index(1)           # select 新着
        webElements = self.GetWebElements(ElementType.Class, "item_title", 10)
        webNewElements = self.GetWebElements(ElementType.Class, "new", 10)
        NewProjectsName = []
        for i in range(len(webNewElements)):             # only append new projects
            NewProjectsName.append(webElements[i].text)
        NewProjectsID = myDataOperation.CreateAnkenID(NewProjectsName)                  # create ID
        NewProjectsURL = []
        for i in range(len(NewProjectsName)):                   # get new project's url
            NewProjectsURL.append(webElements[i].find_element_by_tag_name("a").get_attribute("href"))
        return NewProjectsID, NewProjectsName, NewProjectsURL

    # all process from getting information
    def GetAllInformation(self):
        myDataOperation = DataOperation()           # create new instance of DataOperation
        ALlAnkenName = self.GetALlAnkenName()  # get all of project's name
        AllAnkenURL = self.GetAllAnkenURLs()  # get all of project's URL
        ALlAnkenID = myDataOperation.CreateAnkenID(AllAnkenURL)  # create ID list for json
        return ALlAnkenID, ALlAnkenName, AllAnkenURL

    # close chrome instance
    def CloseChrome(self):
        self.driver.close()

# Class which operate data
class DataOperation:
    # Convert data to JSON style
    def ConvertJSON(self, originalList):
        return jsonify({'projects': originalList})

    # create a list for JSON
    def CreateDict(self, AllAnkenID, AllAnkenName, AllAnkenURL):
        AllInfo = []
        for i in range(len(AllAnkenID)):
            AllInfo.append(
                "{id: " + str(AllAnkenID[i]) + ", title: " + AllAnkenName[i] + ", url: " + AllAnkenURL[i] + "}")
        return AllInfo

    # craete ID list for json
    def CreateAnkenID(self, AnkenList):
        IDList = {}
        for i in range(len(AnkenList)):
            IDList[i] = i
        return IDList

