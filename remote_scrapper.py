import requests
from bs4 import BeautifulSoup

def extract_job(url):
  headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'}
  result = requests.get(url, headers = headers)
  #print(result.text)
  soup = BeautifulSoup(result.text, 'html.parser')
  job_container = soup.select("a")
  print(result.status_code)
  return job_container


def get_jobs(word):
  extract_job(f"https://remoteok.com/remote-{word}-jobs")
  