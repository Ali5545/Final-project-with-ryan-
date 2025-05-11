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
            adminvalue = admin.read().splitlines()
            length = len(adminvalue)
            checkuser = adminvalue[0].strip()
            checkpassword = adminvalue[1].strip()
            if username == checkuser and password == checkpassword:
                return render_template("main.html")
            else:
                return render_template("login.html", check = "Password or username wrong")
        else:
            return render_template("login.html", check = "Account doesnt exist, please create an account")
    
@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        check()
        return render_template("signup.html")
@app.route("/information", methods = ["GET","POST"])   
def check():
    global username, password
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    if username == "" or password == "" or email == "":
        return render_template("signup.html")
    else:
        checklen = len(password)
        if checklen < 6:
            return render_template("signup.html")
        else:
            check = email.isdigit()
            if check == True:
                return render_template("signup.html", check = "Email cannot be just numbers")
            else:                
                filename = username + ".doc"
                filename2 = username +"weightinfo" +".doc"
                filename3 = username + "cart" + ".doc"
                filename4 = username + "workout" + ".doc"
                filename5 = username + "food" + ".doc"
                fileexist = bool(path.exists(filename))
                if fileexist == True:
                    return render_template("login.html", check = "Login already exists, please login")
                else:
                    admin = open(filename, "x")
                    admin.write(username + "\n" + password + "\n" + email)
                    admin.close()
                    admin2 = open(filename2,  "x")
                    admin2.close()
                    admin3 = open(filename3, "x")
                    admin3.close()
                    admin4 = open(filename4, "x")
                    admin4.close()
                    admin5 = open(filename5, "x")
                    admin5.close()
                    
        return render_template("information.html")

if __name__ == "__main__":
    app.run()
