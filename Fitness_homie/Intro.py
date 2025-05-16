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
        return render_template("information.html")
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
                    admin3 = open(filename3, "x")
                    admin3.close()
                    admin4 = open(filename4, "x")
                    admin4.close()
                    admin5 = open(filename5, "x")
                    admin5.close()
        return information()       
    
@app.route("/infohome", methods = ["GET", "POST"])
def information():
    filename = username + ".doc"
    if request.method == "POST":
        return render_template("information.html")    
    else:
        age = request.form.get("age")
        feet = request.form.get("Feet")
        inches = request.form.get("Inches")
        weight = request.form.get("weight")
        goal = request.form.get("goal")
        gender = request.form.get("gender")
        if age == "" or feet == "" or inches == "" or weight == "" or goal == "" or int(feet) > 12 or int(feet) < 1:
            return render_template("information.html", check = "Your height must be between 1 and 12 Feet")
        else:
            check = list(age)
            for i in range(len(check)):
                num = ord(check[i])
                if num < 48 or num > 57:
                    return render_template("information.html", check = "You must type in a number for your age!")
            check2 = list(feet)
            for i in range(len(check2)):
                num2 = ord(check2[i])
                if num2  < 48 or num2 > 57:
                    return render_template("information.html", check = "You must type in a number for your Height!")
            check3 = list(inches)
            for i in range(len(check3)):
                num3 = ord(check3[i])
                if num3 < 48 or num3 > 57:
                    return render_template("information.html", check = "You must type in a number for your Height!")
            check4 = list(weight)
            for i in range(len(check4)):
                num4 = ord(check4)
                if num4 < 48 or num4 > 57:
                     return render_template("information.html", check = "You must type in a number for your weight!")
            height = int(feet) * 12 + int(inches)
            if gender == "Man":
                Bmr = 66.47 + 6.24 * int(weight) + 12.7 * int(height) - 6.755 * int(age)
            else:
                Bmr = 655.1 + 4.35 * int(weight) + 4.7 * int(height) - 4.7 * int(age)

        return render_template("main.html")


           
@app.route("/home", methods = ["GET", "POST"])
def home():
    return render_template("main.html")

@app.route("/profile", methods = ["GET", "POST"])
def profile():
    return render_template("main.html")
if __name__ == "__main__":
    app.run()
