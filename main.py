from flask import Flask, render_template, request
from standard_function import ChromeOperation, DataOperation
import os

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False         # change character code

@app.route("/")
def CW_AllTopProjects():            # get all of VBA projects
    myChromeOperation = ChromeOperation()                   # create new instance of ChromeOperation
    myDataOperation = DataOperation()                   # create new instance of DataOperation
    ALlAnkenID, ALlAnkenName, AllAnkenURL = myChromeOperation.GetAllInformation()                   # get information id, title, url
    myChromeOperation.CloseChrome                   # close chrome instance
    infoDict = myDataOperation.CreateDict(ALlAnkenID, ALlAnkenName, AllAnkenURL)        # create lists for JSON
    jsonData = myDataOperation.ConvertJSON(infoDict)            # convert to JSON style
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/vba/all/")
def CW_AllVBAProjects():            # get all of VBA projects
    myChromeOperation = ChromeOperation()                   # create new instance of ChromeOperation
    myDataOperation = DataOperation()                   # create new instance of DataOperation
    myChromeOperation.SearchKeyword("VBA")              # keyword search
    ALlAnkenID, ALlAnkenName, AllAnkenURL = myChromeOperation.GetAllInformation()                   # get information id, title, url
    myChromeOperation.CloseChrome                   # close chrome instance
    infoDict = myDataOperation.CreateDict(ALlAnkenID, ALlAnkenName, AllAnkenURL)        # create lists for JSON
    jsonData = myDataOperation.ConvertJSON(infoDict)            # convert to JSON style
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/python/all/")
def CW_AllPythonProjects():     # get all of Python projects
    myChromeOperation = ChromeOperation()                   # create new instance of ChromeOperation
    myDataOperation = DataOperation()                   # create new instance of DataOperation
    myChromeOperation.SearchKeyword("Python")              # keyword search
    ALlAnkenID, ALlAnkenName, AllAnkenURL = myChromeOperation.GetAllInformation()                   # get information id, title, url
    myChromeOperation.CloseChrome                   # close chrome instance
    infoDict = myDataOperation.CreateDict(ALlAnkenID, ALlAnkenName, AllAnkenURL)        # create lists for JSON
    jsonData = myDataOperation.ConvertJSON(infoDict)            # convert to JSON style
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/api/all/")
def CW_AllAPIProjects():        # get all of API projects
    myChromeOperation = ChromeOperation()                   # create new instance of ChromeOperation
    myDataOperation = DataOperation()                   # create new instance of DataOperation
    myChromeOperation.SearchKeyword("API")              # keyword search
    ALlAnkenID, ALlAnkenName, AllAnkenURL = myChromeOperation.GetAllInformation()                   # get information id, title, url
    myChromeOperation.CloseChrome                   # close chrome instance
    infoDict = myDataOperation.CreateDict(ALlAnkenID, ALlAnkenName, AllAnkenURL)        # create lists for JSON
    jsonData = myDataOperation.ConvertJSON(infoDict)            # convert to JSON style
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/vba/new/")
def CW_NewVBAProjects():        # get new vba projects
    myChromeOperation = ChromeOperation()                   # create new instance of ChromeOperation
    myDataOperation = DataOperation()                   # create new instance of DataOperation
    myChromeOperation.SearchKeyword("VBA")              # keyword search
    NewProjectsID, NewProjectsName, NewProjectsURL = myChromeOperation.GetNewProjectsInformation()                   # get information id, title, url
    myChromeOperation.CloseChrome                   # close chrome instance
    infoDict = myDataOperation.CreateDict(NewProjectsID, NewProjectsName, NewProjectsURL)        # create lists for JSON
    jsonData = myDataOperation.ConvertJSON(infoDict)            # convert to JSON style
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/python/new/")
def CW_NewPythonProjects():        # get new vba projects
    myChromeOperation = ChromeOperation()                   # create new instance of ChromeOperation
    myDataOperation = DataOperation()                   # create new instance of DataOperation
    myChromeOperation.SearchKeyword("Python")              # keyword search
    NewProjectsID, NewProjectsName, NewProjectsURL = myChromeOperation.GetNewProjectsInformation()                   # get information id, title, url
    myChromeOperation.CloseChrome                   # close chrome instance
    infoDict = myDataOperation.CreateDict(NewProjectsID, NewProjectsName, NewProjectsURL)        # create lists for JSON
    jsonData = myDataOperation.ConvertJSON(infoDict)            # convert to JSON style
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/api/new/")
def CW_NewAPIProjects():        # get new vba projects
    myChromeOperation = ChromeOperation()                   # create new instance of ChromeOperation
    myDataOperation = DataOperation()                   # create new instance of DataOperation
    myChromeOperation.SearchKeyword("API")              # keyword search
    NewProjectsID, NewProjectsName, NewProjectsURL = myChromeOperation.GetNewProjectsInformation()                   # get information id, title, url
    myChromeOperation.CloseChrome                   # close chrome instance
    infoDict = myDataOperation.CreateDict(NewProjectsID, NewProjectsName, NewProjectsURL)        # create lists for JSON
    jsonData = myDataOperation.ConvertJSON(infoDict)            # convert to JSON style
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/search/<keyword>/")
def CW_KeywordSearch(keyword):
    myChromeOperation = ChromeOperation()                   # create new instance of ChromeOperation
    myDataOperation = DataOperation()                   # create new instance of DataOperation
    myChromeOperation.SearchKeyword(keyword)              # keyword search
    ALlAnkenID, ALlAnkenName, AllAnkenURL = myChromeOperation.GetAllInformation()                   # get information id, title, url
    myChromeOperation.CloseChrome                   # close chrome instance
    infoDict = myDataOperation.CreateDict(ALlAnkenID, ALlAnkenName, AllAnkenURL)        # create lists for JSON
    jsonData = myDataOperation.ConvertJSON(infoDict)            # convert to JSON style
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))