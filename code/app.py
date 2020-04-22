from flask import Flask

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return "Hello"


app.run("127.0.0.1")
