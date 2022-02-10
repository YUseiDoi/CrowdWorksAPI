from flask import Flask, render_template, request
from standard_function import InitCrowdworks, SearchKeyword, GetALlAnkenName, GetNewProjects, ConvertJSON, CreateDict, GetAllAnkenURLs, CreateAnkenID, GetInfoAndCreateJSON

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False         # change character code

@app.route("/vba/all/")
def CW_AllVBAProjects():    # get all of VBA projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "VBA")        # keyword search
    jsonData = GetInfoAndCreateJSON(driver)            # get information and create json data
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/python/all/")
def CW_AllPythonProjects():     # get all of Python projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "Python")        # keyword search
    jsonData = GetInfoAndCreateJSON(driver)            # get information and create json data
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/api/all/")
def CW_AllAPIProjects():        # get all of API projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "API")        # keyword search
    jsonData = GetInfoAndCreateJSON(driver)            # get information and create json data
    return render_template('index.html', status_code=("status_code: " + str(jsonData.status_code)), json_data=jsonData.json)

@app.route("/vba/new/")
def CW_NewVBAProjects():        # get new vba projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "VBA")        # keyword search
    newProjects = GetNewProjects(driver)     # get new projects
    driver.close()
    return render_template('index.html', data=zip(newProjects))

@app.route("/python/new/")
def CW_NewPythonProjects():        # get new vba projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "Python")        # keyword search
    newProjects = GetNewProjects(driver, "Python")     # get new projects
    driver.close()
    return render_template('index.html', data=zip(newProjects))

@app.route("/api/new/")
def CW_NewAPIProjects():        # get new vba projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "API")        # keyword search
    newProjects = GetNewProjects(driver, "API")     # get new projects
    driver.close()
    return render_template('index.html', data=zip(newProjects))

@app.route("/search/")
def CW_KeywordSearch():
    keyword = request.args.get("keyword")       # get keyword from parameter
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, keyword)        # keyword search
    eachAnkenName = GetALlAnkenName(driver)          # get projects name
    driver.close()
    return render_template('index.html', data=zip(eachAnkenName))

