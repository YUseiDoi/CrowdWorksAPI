from flask import Flask, render_template
from standard_function import InitCrowdworks, SearchKeyword, GetALlAnkenName, GetNewProjects

app = Flask(__name__)

@app.route("/vba/all/")
def CW_AllVBAProjects():    # get all of VBA projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "VBA")        # keyword search
    eachAnkenName = GetALlAnkenName(driver)         # get all of project's name
    driver.close()
    return render_template('index.html', data=zip(eachAnkenName))

@app.route("/python/all/")
def CW_AllPythonProjects():     # get all of Python projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "Python")        # keyword search
    eachAnkenName = GetALlAnkenName(driver)         # get all of project's name
    driver.close()
    return render_template('index.html', data=zip(eachAnkenName))

@app.route("/api/all/")
def CW_AllAPIProjects():        # get all of API projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    SearchKeyword(driver, "API")        # keyword search
    eachAnkenName = GetALlAnkenName(driver)         # get all of project's name
    driver.close()
    return render_template('index.html', data=zip(eachAnkenName))

@app.route("/vba/new/")
def CW_NewVBAProjects():        # get new vba projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    newProjects = GetNewProjects(driver, "VBA")     # get new projects
    driver.close()
    return render_template('index.html', data=zip(newProjects))

@app.route("/python/new/")
def CW_NewPythonProjects():        # get new vba projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    newProjects = GetNewProjects(driver, "Python")     # get new projects
    driver.close()
    return render_template('index.html', data=zip(newProjects))

@app.route("/api/new/")
def CW_NewAPIProjects():        # get new vba projects
    driver = InitCrowdworks()       # Init Chrome instance and go to CrowdWorks
    newProjects = GetNewProjects(driver, "API")     # get new projects
    driver.close()
    return render_template('index.html', data=zip(newProjects))

