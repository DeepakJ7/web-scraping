from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import os


# OPENING CHROME AND WEBSITE
options = Options()
options.add_argument("--headless=new")
driver1 = webdriver.Chrome(options=options)
#driver1 = webdriver.Chrome('C:/Users/deepa/Downloads/chromedriver_win32/chromedriver.exe')
driver1.get('https://www.naukri.com/')
driver1.maximize_window()
print("opening website")
time.sleep(1)

# CLOSING THE COOKIE
driver1.find_element(By.XPATH,'//*[@id="root"]/div[6]/div/span').click()
print("close cookie")

# FINDING AND TYPING IN THE SEARCH BAR
box1 = driver1.find_element(By.XPATH,'//*[@id="root"]/div[6]/div/div[1]/div[1]/div/div/div/div[1]/div/input')
print("found")
time.sleep(1)
query = 'Web Scraping'
for i in query:
    box1.send_keys(i)
    time.sleep(1)
print('type finished')
time.sleep(1)

# SELECTION OF THE EXPERIENCE SELECTOR
driver1.find_element(By.XPATH,'//*[@id="root"]/div[6]/div/div[1]/div[3]/div/span').click()
print('scroll selector selected')
time.sleep(1)

# SELECTION OF FRESHER
driver1.find_element(By.XPATH,'//*[@id="sa-dd-scrollexpereinceDD"]/div[1]/ul/li[1]').click()
print('fresher selected')
time.sleep(1)

# ENTERING THE DESIRED LOCATION
box2 = driver1.find_element(By.XPATH,'//*[@id="root"]/div[6]/div/div[1]/div[5]/div/div/div/div[1]/div/input')
print('enter location found')
time.sleep(1)
query = 'Bangalore'
for i in query:
    box2.send_keys(i)
    time.sleep(1)
print('location type finished')
time.sleep(1)

# PRESSING ENTER FOR THE COMMENCE OF SEARCH
driver1.find_element(By.XPATH,'//*[@id="root"]/div[6]/div/div/div[6]').click()
print('entered search')
time.sleep(1)

# WE TAKE LINKS FROM NAUKRI.COM AND STORE THEM IN 'LINKS' LIST
#links=[]
articles=[]
#url = driver1.find_elements(By.XPATH, '//*[@class="title ellipsis"]')
while(True):
    try:
        time.sleep(2)
        elem = driver1.find_element(By.XPATH, "//a[@class='fright fs14 btn-secondary br2']")
        urls = driver1.find_elements(By.XPATH, '//*[@class="title ellipsis"]')
        for url in urls:
            articles.append(url.get_attribute("href"))
            print(articles)
            print(len(articles))
        if (len(articles)<25):
            elem.click()
        else:
            break
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,
           ElementClickInterceptedException) as ex:
        print("breaking as there is no next page")
        break

list_of_skills=[]
for url in articles:
    driver1.get(url)
    divs = driver1.find_elements(By.XPATH, '//div[@class="key-skill"]//a')
    for div in divs:
        text = div.find_element(By.XPATH, './span').text
        list_of_skills.append(text)
        print(text)
        text = text.replace("\n", ' ')
    list_of_skills1 = list(set(list_of_skills))
    import pandas as pd

    df = pd.DataFrame(list_of_skills1, columns=['list of skills'])
    df.to_excel("skill-req.xlsx")
