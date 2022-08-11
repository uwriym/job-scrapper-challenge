from wework_scrapper import get_jobs as wework_get_jobs
from so_scrapper import get_jobs as so_get_jobs
from remote_scrapper import get_jobs as remote_get_jobs
from flask import Flask, render_template, request, redirect, send_file

def get_jobs(word):
  jobs = wework_get_jobs(word) + so_get_jobs(word)
  return jobs

#print(get_jobs("react"))
  
#print(wework_get_jobs("python"))
#print(so_get_jobs("python"))
#print(remote_get_jobs("python"))

app = Flask("ElegantScrapper")

db = {}

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    exsistingJobs = db.get(word)
    if exsistingJobs:
      jobs = exsistingJobs
    else:
      jobs = get_jobs(word)
      db[word] = jobs
  else:
    return redirect("/")
  return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")

app.run(host="0.0.0.0")