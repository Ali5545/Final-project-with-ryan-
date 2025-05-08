from flask import Flask, request, render_template, redirect,url_for
import os.path
from os import path

app = Flask(__name__)
@app.route("/", methods = ["GET","POST"])

def main():
    if request.method == "GET":
        return render_template("login.html")
    else:
        checklogin()
        return render_template("login.html")
@app.route("/mainpage", methods = ["GET","POST"])
def checkogin():
    global username, password
    fileDir = os.path.dirname(os.path.realpath("__file__"))

    username = request.form.get("username")
    password = request.form.get("password")

    if (username == "" or password == ""):
        return render_template("login.html")
    else:
        filename = username + ".doc"
        fileexist = bool(path.exists(filename))
        if fileexist == True:
            admin = open(filename, "r")
            adminvalue = admin.read().striplines()

            checkuser = adminvalue.strip(0)
            checkpassword = adminvalue.strip(1)
            if username == checkuser and password == checkpassword:
                return render_template("main.html")
            else:
                return render_template("login.html", check = "Password wrong")
        else:
            return render_template("login.html", check = "Account doesnt exist")


        
    
@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        information()
        return render_template("signup.html")

    
@app.route("/signupinformation", methods = ["GET","POST"])
def information():
    return render_template("information.html")

if __name__ == "__main__":
    app.run()
