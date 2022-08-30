from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
"""from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")"""


# def extract_jobs_indeed(keyword):
browser = webdriver.Chrome(
    # options=options
)

browser.get("https://www.indeed.com/jobs?q=python&limit=50")
# while (True):
#    pass

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find('ul', class_="jobsearch-ResultsList")
jobs = job_list.find_all('li', recursive=False)
for job in jobs:
    print(job)
    print("------")
