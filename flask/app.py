from flask import Flask, render_template

app = Flask("SuperScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<username>")
def contact(username):
    return f"Contact {username}"


app.run()
