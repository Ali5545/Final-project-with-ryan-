from flask import Flask, request, render_template, redirect,url_for
import os.path
from os import path

app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])

def main():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return render_template("login.html")

@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        return render_template("signup.html")

if __name__ == "__main__":
    app.run()
