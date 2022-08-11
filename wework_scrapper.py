import requests
from bs4 import BeautifulSoup

def extract_job(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  job_container = soup.select("section.jobs ul > li")
  jobs = []
  print("Scrapping WeWork")
  for job in job_container:
    title = job.select_one("a > span.title")
    if title is not None:
      title = title.text
    else:
      pass
    company = job.select_one("a > span.company")
    if company is not None:
      company = company.text
    else:
      pass
    location = job.select_one("a > span.region")
    if location is not None:
      location = location.text
    else:
      pass
    
    link = job.find("a", recursive=False)["href"]
    
    if link is None:
      pass
    job_info = {}
    job_info["title"] = title
    job_info["company"] = company
    job_info["location"] = location
    job_info["apply_link"] = f"https://weworkremotely.com{link}"
    jobs.append(job_info)
  
    for j in jobs:
      if j["apply_link"] == 'https://weworkremotely.com//categories/remote-full-stack-programming-jobs':
        j["title"] = "Full Stack Programming Jobs"
      elif j["apply_link"] == 'https://weworkremotely.com//categories/remote-back-end-programming-jobs':
        j["title"] = "Back End Programming Jobs"
      elif j["apply_link"] == 'https://weworkremotely.com//categories/all-other-remote-jobs':
        j['title'] = "All Other Remote Jobs"
      elif j["apply_link"] == 'https://weworkremotely.com//categories/remote-design-jobs':
        j["title"] = "Design Jobs"
    
  return jobs
  


def get_jobs(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  jobs = extract_job(url)
  return jobs

#print(get_jobs(python))
  