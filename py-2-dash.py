from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.common.keys import Keys
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

app = Dash()

job_options = [
    {'label': 'Software Engineer', 'value': 'software-engineer'},
    {'label': 'Data Analyst', 'value': 'data-analyst'},
    {'label': 'Cybersecurity analyst', 'value': 'cybersecurity-analyst'},
    {'label': 'Network Administrator', 'value': 'network-administrator'},
    {'label': 'Systems Administrator', 'value': 'systems-administrator'},
    {'label': 'Database Administrator', 'value': 'database-administrator'},
    {'label': 'IT Project Manager', 'value': 'IT-project-manager'},
    {'label': 'Web Developer', 'value': 'web-developer'},
    {'label': 'Cloud Architect', 'value': 'cloud-architect'},
    {'label': 'Artificial Intelligence Engineer', 'value': 'artificial-intelligence-engineer'},
    {'label': 'DevOps Engineer', 'value': 'devops-engineer'},
    {'label': 'IT Consultant', 'value': 'it-consultant'},
    {'label': 'IT Business Analyst', 'value': 'it-business-analyst'},
    {'label': 'IT Support Specialist', 'value': 'it-support-specialist'},
    {'label': 'IT Auditor', 'value': 'it-auditor'},
    {'label': 'IT Trainer', 'value': 'it-trainer'},
    {'label': 'UI/UX Designer', 'value': 'ui/ux-designer'},
    {'label': 'Mobile App Developer', 'value': 'mobile-app -developer'},
    {'label': 'Big Data Engineer', 'value': 'big-data-engineer'},
    {'label': 'Blockchain Developer', 'value': 'blockchain-developer'},
    {'label': 'IT Sales Professional', 'value': 'it-sales-professional'},
    {'label': 'IT Service Manager', 'value': 'it-service-manager'},
    {'label': 'IT Risk Manager', 'value': 'it-risk-manager'},
    {'label': 'IT Procurement Specialist', 'value': 'it-procurement-specialist'},
    {'label': 'IT Compliance Analyst', 'value': 'it-compliance-analyst'},
    {'label': 'IT Operations Manager', 'value': 'it-operations-manager'},
    {'label': 'IT Quality Assurance Analyst', 'value': 'it-quality Assurance Analyst'},
    {'label': 'IT Technical Writer', 'value': 'it-technical-writer'},
    {'label': 'IT Change Manager', 'value': 'it-change-manager'},
    {'label': 'IT Vendor Manager', 'value': 'it-vendor-manager'},
]

search = dcc.Dropdown(id="input-search-term", options=job_options, value="software-engineer")

app.layout = html.Div(
    children=[
        html.H1("Job Search"),
        html.Label("Select a job:"),
        search,
        html.Button("Search", id="btn-search", n_clicks=0),
        html.H2("Top 40 Job Links:"),
        html.Ul(id="articles"),
    ]
)

@app.callback(
    Output("articles", "children"),
    [Input("btn-search", "n_clicks")],
    [Input("input-search-term", "value")]
)

def perform_search(articles , options):
    options = Options()
    options.add_argument("--headless=new")
    driver1 = webdriver.Chrome(options=options)
    # driver1 = webdriver.Chrome('C:/Users/deepa/Downloads/chromedriver_win32/chromedriver.exe')
    driver1.get('https://www.naukri.com/')
    driver1.maximize_window()
    driver1.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/span').click()
    box1 = driver1.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div[1]/div[1]/div/div/div/div[1]/div/input')
    query = {search}
    for i in query:
        box1.send_keys(i)
    driver1.find_element(By.XPATH, '//*[@id="root"]/div[6]/div/div/div[6]').click()
    time.sleep(5)
    #box2 = driver1.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div/section[1]/div[2]/div[4]/div[2]/div[1]/label/i').click()
    articles = []
    url = driver1.find_elements(By.XPATH, '//*[@class="title ellipsis"]')
    while (True):
        try:
            time.sleep(2)
            elem = driver1.find_element(By.XPATH, "//a[@class='fright fs14 btn-secondary br2']")
            urls = driver1.find_elements(By.XPATH, '//*[@class="title ellipsis"]')
            for url in urls:
                href = articles.append(url.get_attribute("href"))
                print(len(articles))
                print(articles)
            if (len(articles) < 40):
                elem.click()
            else:
                break
        except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
               ElementClickInterceptedException) as ex:
            print("breaking as there is no next page")
            break
    return articles

if __name__ == "__main__":
    app.run_server(debug=True)
