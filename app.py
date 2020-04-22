from flask import Flask, render_template, request, redirect
from scrapper.so import get_jobs

app = Flask("SuperScrapper")

db = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        jobs = get_jobs(word)
        db[word] = jobs
    else:
        redirect("/")
    return render_template("report.html", searchingBy=word)


app.run()
