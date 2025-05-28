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
    global status
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
                status = "home"
                return which()
            else:
                return render_template("login.html", check = "Password or username wrong")
        else:
            return render_template("login.html", check = "Account doesnt exist, please create an account")
    
@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        return check()
@app.route("/information", methods = ["GET", "POST"])
def check():
    global username, password
    if request.method == "POST":
        print("Im working")
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
                        admin5.write("0" + "\n" + "0" + "\n" + "0" + "\n" + "0")
                        admin5.close()
            return render_template("information.html")    
    else:
        return check2()
@app.route("/infohome", methods = ["GET", "POST"])
def check2():
    global status
    age = request.form.get("age")
    feet = request.form.get("Feet")
    inches = request.form.get("Inches")
    weight = request.form.get("weight")
    goal = request.form.get("goal")
    gender = request.form.get("gender")
    if age == "" or feet == "" or inches == "" or weight == "" or goal == "":
        return render_template("information.html", check = "You must type something into all of the input boxes!!")
    else:
        if int(feet) > 12 or int(feet) < 1:
            return render_template("information.html", check = "The feet part of your height must be between 1 and 12 feet")
        else:
            if int(inches) > 12 or int(inches) < 1:
                return render_template("information.html", check = "The inches part of your height must be between 1 and 12 inches!!")
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
                    num4 = ord(check4[i])
                    if num4 < 48 or num4 > 57:
                        return render_template("information.html", check = "You must type in a number for your weight!")
        height = int(feet) * 12 + int(inches)
        if gender == "Man":
            Bmr = 66.47 + (6.24 * int(weight) )+ (12.7 * int(height)) - (6.76 * int(age))
        else:
            Bmr = 655 + (4.34 * int(weight)) + (4.7 * int(height)) - (4.7 * int(age))

        if goal == "Lose weight/Fat" :
            Cal_intake = round(Bmr) - 300
        else:
            Cal_intake = round(Bmr) + 300
        filename = username + ".doc"
        admin = open(filename, "a")
        admin.write("\n" + str(age) + "\n" + str(height) + "\n" + str(weight) + "\n" + str(goal) + "\n" + str(gender) + "\n" + str(round(Bmr)) + "\n" + str(Cal_intake))
        admin.close()
        status = "home"
        return which()
        
def which():
    global base_cal, base_carbs, base_protein, base_fat
    print("works")
    filename1 = username + ".doc"
    filename2 = username + "food" + ".doc"
    
    admin = open(filename1, "r")
    adminvalue = admin.read().splitlines()
    admin.close()
    base_cal = adminvalue[9].strip()
    base_carbs = round((float(base_cal) * float(0.45)) / 4)
    base_protein = round((float(base_cal) * float(0.25)) /4)
    base_fat = round((float(base_cal) * float(0.30))/9)

    admin2 = open(filename2 , "r")
    admin2value = admin2.read().splitlines()
    admin2.close()

    intake_cal = admin2value[0].strip()
    intake_protein = admin2value[1].strip()
    intake_carbs = admin2value[2].strip()
    intake_fats = admin2value[3].strip()
    
    remaining_cal = int(base_cal) - int(intake_cal)
    remaining_protein = int(base_protein) - int(intake_protein)
    remaining_carbs = int(base_carbs) - int(intake_carbs)
    remaining_fats = int(base_fat) - int(intake_fats)
    match(status):
        case "home":
            return render_template("main.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats)
        case "macro_tracker":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats)
        case "newday":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                        status = "Started New day!")
        case "updated":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                        status = "Updated your macros!")
        case "check":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                        status = "You must type in numbers for your fats, carbs and proteins!")
        case "check1":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                        status = "You must fill in all boxes!")
        case default:
            return render_template("main.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats)            
            
@app.route("/home", methods = ["GET", "POST"])
def home():
    print("works")
    filename1 = username + ".doc"
    filename2 = username + "food" + ".doc"
    
    admin = open(filename1, "r")
    adminvalue = admin.read().splitlines()
    admin.close()
    base_cal = adminvalue[9].strip()
    base_carbs = round((float(base_cal) * float(0.45)) / 4)
    base_protein = round((float(base_cal) * float(0.25)) /4)
    base_fat = round((float(base_cal) * float(0.30))/9)

    admin2 = open(filename2 , "r")
    admin2value = admin2.read().splitlines()
    admin2.close()

    intake_cal = admin2value[0].strip()
    intake_protein = admin2value[1].strip()
    intake_carbs = admin2value[2].strip()
    intake_fats = admin2value[3].strip()
    
    remaining_cal = int(base_cal) - int(intake_cal)
    remaining_protein = int(base_protein) - int(intake_protein)
    remaining_carbs = int(base_carbs) - int(intake_carbs)
    remaining_fats = int(base_fat) - int(intake_fats)
    return render_template("main.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats)

@app.route("/profile", methods = ["GET", "POST"])
def profile():
    filename1 = "Profile.txt"
    filename2 = username + ".doc"

    admin1 = open(filename1, "r")
    admin1value = admin1.read().split(",")
    length = len(admin1value)
    admin1.close()

    admin2 = open(filename2, "r")
    admin2value = admin2.read().splitlines()
    admin2.close()
    
    return render_template("profile.html", length = length, Category = admin1value, information = admin2value )
@app.route("/macro_tracker", methods = ["GET", "POST"])
def macro_tracker():
    global status
    print("hello")
    new_total_cal = 0
    new_total_pro = 0
    new_total_carb = 0
    new_total_fats = 0

    filename = username + "food" + ".doc"
    if request.method == "GET":
        status = "macro_tracker"   
        return which()
    else:
        button_press = request.form.get("submit")
        match(button_press):
            case "Input":
                carbs = request.form.get("carbnum")
                protein = request.form.get("proteinnum")
                fats = request.form.get("fatnum")
                foodname = request.form.get("foodname")
                print(carbs,protein, fats, foodname)
                if carbs == "" or protein == "" or fats == "" or foodname == "":
                    status = "check1"   
                    return which()
                else:
                    list1 = list(carbs)
                    for i in range(0, len(list1)):
                        check1 = ord(list1[i])
                        if check1 < 48 or check1 > 57:
                            status = "check"
                            return which()
                    list2 = list(protein)
                    for i in range(0,len(list2)):
                        check2 = ord(list2[i])
                        if check2 < 48 or check2 > 57:
                            status = "check"
                            return which()
                    list3 = list(fats)
                    for i in range(0,len(list3)):
                        check3 = ord(list3[i])
                        if check3 < 48 or check3 > 57:
                            status = "check"
                            return which()

                    mealcal = (int(protein) * 4) + (int(carbs) * 4) + (int(fats) * 9)
                    admin = open(filename, "r")
                    adminvalue = admin.read().splitlines()
                    admin.close()
                    totalcal = adminvalue[0].strip()
                    new_total_cal = int(totalcal) + mealcal

                    total_pro = adminvalue[1].strip()
                    new_total_pro = int(total_pro) + int(protein)

                    total_carb = adminvalue[2].strip()
                    new_total_carb = int(total_carb) + int(carbs)

                    total_fats = adminvalue[3].strip()
                    new_total_fats = int(total_fats) + int(fats)

                    remaining_cal = int(base_cal) - int (new_total_cal)
                    remaining_protein = int(base_protein) - int(new_total_pro)
                    remaining_carbs = int(base_carbs) - int(new_total_carb)
                    remaining_fats = int(base_fat) - int(new_total_fats)
                    
                    admin2 = open(filename, "w")
                    admin2.write(str(new_total_cal) + "\n" + str(new_total_pro) + "\n" + str(new_total_carb) + "\n" + str(new_total_fats))
                    admin2.close()
                    status = "updated"
                    return redirect(url_for("macro_tracker"))  
            case "newday":
                admin = open(filename, "w")
                admin.write("0" + "\n" + "0" + "\n" + "0" + "\n" + "0")
                admin.close()
                status = "newday"
                return redirect(url_for("macro_tracker"))  
            case default:
                status = "macro_tracker"
                return home()
        return which()

if __name__ == "__main__":
    app.run()
