import requests
from bs4 import BeautifulSoup


def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  pages = soup.select("div.s-pagination>a>span")
  last_page = pages[-2].text
  return int(last_page)

def extract_job(html):
  title = html.select_one("h2.mb4>a[title]").text
  company, location = html.select_one("h3.mb4").find_all("span", recursive=False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)
  job_id = html["data-jobid"]

  return {"title": title, "company": company, "location": location, "apply_link":f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page, url):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping SO page{page+1}")
    result = requests.get(f"{url}{page+1}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.select("div[data-jobid]")
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs
    
  

def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?q={word}&pg="
  last_page = get_last_page(url)
  jobs = extract_jobs(last_page, url)
  return jobs