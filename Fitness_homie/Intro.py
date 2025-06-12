from flask import Flask, request, render_template, redirect,url_for
import os.path
from os import path
#Admin username and password:
#Username: Admin
#Password: Admin
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
    filename2 = "usernames.txt"
    exist = bool(path.exists(filename2))
    if exist == False:
        file = open(filename2, "x")
        file.close()
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
            if username == "Admin" and password == "Admin":
                return admin_page()
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
        fileDir = os.path.dirname(os.path.realpath("__file__"))
        filename2 = "usernames.txt"
        exist = bool(path.exists(filename2))
        if exist == False:
            file = open(filename2, "x")
            file.close()            
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
                    filename3 = username + "past" + ".doc"
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
                        admin4.write("1" + "\n")
                        admin4.close()
                        admin5 = open(filename5, "x")
                        admin5.write("0" + "\n" + "0" + "\n" + "0" + "\n" + "0" + "\n" + "0"+ "\n" + "1")
                        admin5.close()
                        admin6 = open(filename2, "a")
                        admin6.write(username + "\n")
                        admin6.close()
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
            if int(inches) > 12 or int(inches) < 0:
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
#Main Pages        
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
    meal_number = admin2value[4].strip()
    day = admin2value[5].strip()
    match(status):
        case "home":
            return render_template("main.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                                   number = meal_number, day = day)
        case "macro_tracker":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                                   number = meal_number, day = day)
        case "newday":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                        status = "Started New day!",number = meal_number, day = day)
        case "updated":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                        status = "Updated your macros!",number = meal_number, day = day)
        case "check":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                        status = "You must type in numbers for your fats, carbs and proteins!",number = meal_number, day = day)
        case "check1":
            return render_template("macro_tracker.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                        status = "You must fill in all boxes!",number = meal_number, day = day)
        case default:
            return render_template("main.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                        proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                        carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                                   number = meal_number, day = day)            
#Home page    
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
    meal_number = admin2value[4].strip()
    day = admin2value[5].strip()
    return render_template("main.html", caloriestotal = base_cal, calories = intake_cal, recommendedCals = remaining_cal,
                proteintotal = base_protein, proteins = intake_protein, recommendedPro = remaining_protein, carbsintake = base_carbs,
                carbs = intake_carbs, recommendedCarbs = remaining_carbs, fatintake = base_fat, fats = intake_fats, recommendedFats = remaining_fats,
                           number = meal_number, day = day)

#Profile page
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

#Macro Tracker
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

                    meal = adminvalue[4].strip()
                    newmeal = int(meal) + 1

                    day = adminvalue[5].strip()
                    admin2 = open(filename, "w")
                    admin2.write(str(new_total_cal) + "\n" + str(new_total_pro) + "\n" + str(new_total_carb) + "\n" + str(new_total_fats) + "\n" + str(newmeal) + "\n" + str(day))
                    admin2.close()
                    status = "updated"
                    return redirect(url_for("macro_tracker"))  
            case "newday":
                admin1 = open(filename, "r")
                adminvalue = admin1.read().splitlines()
                admin1.close()
                day = adminvalue[5].strip()
                new_day = int(day) + 1
                admin = open(filename, "w")
                admin.write("0" + "\n" + "0" + "\n" + "0" + "\n" + "0" + "\n" + "0" + "\n" + str(new_day))
                admin.close()
                status = "newday"
                return redirect(url_for("macro_tracker"))  
            case default:
                status = "macro_tracker"
                return home()
        return which()
#workout Tracker
@app.route("/workout_tracker", methods = ["GET", "POST"])
def workout_tracker():
    global status2
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    filename = username + "workout" + ".doc"
    filename2 = username + "past" + ".doc"
    if request.method == "GET":
        status2 = "workout_tracker"
        return which2()
    else:
        which_one = request.form.get("submit")
        match (which_one):
            case "Input":
                exercise = request.form.get("exercise")
                sets = request.form.get("sets")
                reps = request.form.get("reps")
                weight = request.form.get("Weight")
                if exercise == "" or sets == "" or reps == "" or weight == "":
                    status2 = "check1"
                    return which2()
                else:
                    check1 = list(sets)
                    for i in range(0,len(check1)):
                        check2 = ord(check1[i])
                        if check2 < 48 or check2 > 57:
                            status2 = "check2"
                            return which2()
                    check3 = list(reps)
                    for i in range(0,len(check3)):
                        check4 = ord(check3[i])
                        if check4 < 48 or check4 > 57:
                            status2 = "check2"
                            return which()
                    check5 = list(weight)
                    for i in range(0, len(check5)):
                        check6 = ord(check5[i])
                        if check6 < 48 or check6 > 57:
                            status2 = "check2"
                            return which()
                admin1 = open(filename, "r")
                admin1value = admin1.read().splitlines()
                admin1.close()
                day = admin1value[0].strip()
                admin = open(filename, "a")
                admin.write(str(exercise) + ":  " + str(weight) + " Lbs for "+  str(sets) + " Sets of " + str(reps) + " Reps" + "\n")
                admin.close()

                return redirect(url_for("workout_tracker"))
            case "newday":
                admin = open(filename, "r")
                adminvalue = admin.read().splitlines()
                admin.close()
                admin2 = open(filename, "r+")
                admin2.truncate()
                admin2.close()
                admin3 = open(filename, "w")
                day = int(adminvalue[0].strip()) + 1
                admin3.write(str(day) + "\n")
                write(adminvalue, filename2)
                return redirect(url_for("workout_tracker"))
        return which2()

def which2():
    past = []
    days = []
    filename = username + "workout" + ".doc"
    filename2 = username + "past" + ".doc"
    admin = open(filename, "r")
    adminvalue = admin.read().splitlines()
    admin.close()
    day = adminvalue.pop(0)
    length = len(adminvalue)
    admin2 = open(filename2, "r")
    admin2value = admin2.read().splitlines()
    for i in range(0,len(admin2value)):
        value = admin2value[i].strip()
        past.append(value)
    length2 = len(past)
    match status2:
        case "check1":
            return render_template("workout_tracker.html", length = length, workout = adminvalue, status = "You must type in an input!", day = day,
                                   length2 = length2, past = past)
        case "check2":
            return render_template("workout_tracker.html", length = length, workout = adminvalue, status = "You must type in a number for sets, reps and weight!",
                                   day = day, length2 = length2, past = past)
        case default:
            return render_template("workout_tracker.html", length = length, workout = adminvalue , day = day, length2 = length2, past = past)

def write(valueadmin, namefile2):
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    exist = bool(path.exists(namefile2))

    if exist == False:
        admin = open(namefile2, "x")
        admin.close()
    else:
        admin = open(namefile2, "a")
        for i in range(0, len(valueadmin)):
            admin.write(str(valueadmin[i]) + "\n")
        admin.close()

#Workout info pages        
@app.route("/workout_info", methods = ["GET", "POST"])
def workout_info():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    names2 = []
    names = ["Chest_day_workout.txt", "Arm_day.txt", "Back_day.txt", "Leg_day.txt"]
    filename = "Core.txt"
    filename2 = "Workout_videos.txt"
    exist = bool(path.exists(filename))
    exist2 = bool(path.exists(filename2))
    if exist == False:
        admin = open(filename, "x")
        admin.close()
    if exist2 == False:
        admin2 = open(filename2, "x")
        admin2.close()
    for i in range(0, len(names)):
        fileexist = bool(path.exists(names[i]))
        if fileexist  == False:
            admin = open(names[i], "x")
            admin.close()
        
    admin5 = open(filename, "r")
    admin5value = admin5.read().splitlines()
    admin5.close()
    length5 = len(admin5value)
    
    admin6 = open(filename2, "r")
    admin6value = admin6.read().splitlines()
    admin6.close()
    length6 = len(admin6value)
    for i in range (0, len(names)):
        admin = open(names[i], "r")
        adminvalue = admin.read().splitlines()
        admin.close()
        names2.append(adminvalue)
    length2 = len(names2)
    return render_template("workoutinformation.html", length2 = length2, groups = names2, length5 = length5, more_info = admin5value,
                           length6 = length6, videos = admin6value)

@app.route("/macro_info", methods = ["GET", "POST"])
def macro_info():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    names = ["protein.txt", "carb.txt", "Fat.txt", "fiber.txt"]
    names2 = []
    filename = "macro_info.txt"
    filename2 = "food_videos.txt"
    exist = bool(path.exists(filename))
    exist2 = bool(path.exists(filename2))
    if exist == False:
        admin = open(filename, "x")
        admin.close()
    if exist2 == False:
        admin2 = open(filename2, "x")
        admin2.close()
    for i in range(0, len(names)):
        exist = bool(path.exists(names[i]))
        if exist == False:
            admin3 = open(names[i], "x")
            admin3.close()
    admin = open(filename, "r")
    adminvalue = admin.read().splitlines()
    admin.close
    length = len(adminvalue)
    
    admin2 = open(filename2, "r")
    admin2value = admin2.read().splitlines()
    admin2.close()
    length3 = len(admin2value)

    for i in range(0,len(names)):
        admin3 = open(names[i], "r")
        admin3value = admin3.read().splitlines()
        admin3.close()
        names2.append(admin3value)
    length2 = len(names2)
    return render_template("macro_information.html", length = length, information = adminvalue, length3 = length3,
                           videos = admin2value, length2 = length2, groups = names2)

#Admin panels
@app.route("/admin_page", methods = ["GET","POST"])
def admin_page():
    user_files = []
    list1 = []
    profile = "Profile.txt"
    filename = "usernames.txt"
    admin = open(filename, "r")
    adminvalue = admin.read().splitlines()
    admin.close()
    
    for i in range(0,len(adminvalue)):
        filename1 = adminvalue[i] + ".doc"
        user_files.append(filename1)
    for i in range(0, len(user_files)):
        admin = open(user_files[i], "r")
        adminvalue = admin.read().splitlines()
        admin.close()
        list1.append(adminvalue)

    admin2 = open(profile, "r")
    admin2value = admin2.read().split(",")
    admin2.close
    length = len(list1)
        
    return render_template("admin.html", length = length, users = list1, headers = admin2value)

@app.route("/edit_food", methods = ["GET", "POST"])
def edit_food():
    global status, names, names2
    names = ["protein.txt", "carb.txt", "Fat.txt", "fiber.txt"]
    names2 = []
    filename = "food_videos.txt"
    if request.method == "GET":
        status = "Load"
        return which3()
    else:
        which_button = request.form.get("submit")
        print(which_button)
        match(which_button):
            case "delete":
                file = request.form.get("whichfile")
                line = request.form.get("delete")
                if file not in names:
                    status = "False_exist"
                    return which3()
                else:
                    if file == "" or line == "":
                        status = "nothing"
                        return which3()
                    else:
                        check1 = list(line)
                        for i in range(len(check1)):
                            check2 = ord(check1[i])
                            if check2 < 48 or check2 > 57:
                                status = "number"
                                return which3()
                        admin = open(file, "r")
                        adminvalue = admin.read().splitlines()
                        admin.close()
                        which_line = int(line)
                        if which_line > len(adminvalue):
                            status = "long"
                            return which3()
                        else: 
                            adminvalue.pop(which_line)
                            admin2 = open(file, "r+")
                            admin2.truncate()
                            admin2.close()
                            for i in range(len(adminvalue)):
                                admin3 = open(file, "a")
                                admin3.write(adminvalue[i] + "\n")
                                admin3.close()
                            return redirect(url_for('edit_food'))
            case "add":
                file = request.form.get("whichfile")
                info = request.form.get("add")
                if file not in names:
                    status = "False_exist"
                    print("Workouts")
                    return which3()
                else:
                    if file == "" or info == "":
                        status = "nothing"
                        return which3()
                    else:
                        admin = open(file, "a")
                        admin.write( info + "\n")
                        admin.close()
                        return redirect(url_for('edit_food'))
            case "delete_video":
                line = request.form.get("delete_video")
                if line == "":
                    status = "nothing"
                    return which3()
                else:
                    check1 = list(line)
                    for i in range(len(check1)):
                        check2 = ord(check1[i])
                        if check2 < 48 or check2 > 57:
                            status = "number"
                            return which3()
                    admin = open(filename, "r")
                    adminvalue = admin.read().splitlines()
                    admin.close
                    number = int(line)
                    if number > len(adminvalue):
                        status = "long"
                        return which3()
                    else:
                        adminvalue.pop(number)
                        admin2 = open(filename, "r+")
                        admin2.truncate()
                        admin2.close()
                        for i in range(len(adminvalue)):
                            admin3 = open(filename, "a")
                            admin3.write(adminvalue[i] + "\n")
                            admin3.close()
                        return redirect(url_for('edit_food'))
            case "add_video":
                info = request.form.get("add_video")
                if info == "":
                    status = "nothing"
                    return which3()
                else:
                    admin = open(filename,  "a")
                    admin.write(info + "\n")
                    admin.close()
                    return redirect(url_for('edit_food'))
            case default:
                return which3()

@app.route("/edit_workout", methods = ["GET", "POST"])
def edit_workout():
    global status2, names, names2
    names = ["Chest_day_workout.txt", "Arm_day.txt", "Back_day.txt", "Leg_day.txt"]
    names2 = []
    filename = "Workout_videos.txt"
    if request.method == "GET":
        status2 = "Load"
        return which4()
    else:
        which_button = request.form.get("submit")
        print(which_button)
        match(which_button):
            case "delete":
                file = request.form.get("whichfile")
                line = request.form.get("delete")
                if file not in names:
                    status2 = "False_exist"
                    return which4()
                else:
                    if file == "" or line == "":
                        status = "nothing"
                        return which4()
                    else:
                        check1 = list(line)
                        for i in range(len(check1)):
                            check2 = ord(check1[i])
                            if check2 < 48 or check2 > 57:
                                status2 = "number"
                                return which4()
                        admin = open(file, "r")
                        adminvalue = admin.read().splitlines()
                        admin.close()
                        which_line = int(line)
                        if which_line > len(adminvalue):
                            status2 = "long"
                            return which4()
                        else: 
                            adminvalue.pop(which_line)
                            admin2 = open(file, "r+")
                            admin2.truncate()
                            admin2.close()
                            for i in range(len(adminvalue)):
                                admin3 = open(file, "a")
                                admin3.write(adminvalue[i] + "\n")
                                admin3.close()
                            return redirect(url_for('edit_workout'))
            case "add":
                file = request.form.get("whichfile")
                info = request.form.get("add")
                if file not in names:
                    status2 = "False_exist"
                    print("Workouts")
                    return which4()
                else:
                    if file == "" or info == "":
                        status2 = "nothing"
                        return which4()
                    else:
                        admin = open(file, "a")
                        admin.write( info + "\n")
                        admin.close()
                        return redirect(url_for('edit_workout'))
            case "delete_video":
                line = request.form.get("delete_video")
                if line == "":
                    status2 = "nothing"
                    return which4()
                else:
                    check1 = list(line)
                    for i in range(len(check1)):
                        check2 = ord(check1[i])
                        if check2 < 48 or check2 > 57:
                            status = "number"
                            return which4()
                    admin = open(filename, "r")
                    adminvalue = admin.read().splitlines()
                    admin.close
                    number = int(line)
                    if number > len(adminvalue):
                        status2 = "long"
                        return which4()
                    else:
                        adminvalue.pop(number)
                        admin2 = open(filename, "r+")
                        admin2.truncate()
                        admin2.close()
                        for i in range(len(adminvalue)):
                            admin3 = open(filename, "a")
                            admin3.write(adminvalue[i] + "\n")
                            admin3.close()
                        return redirect(url_for('edit_workout'))
            case "add_video":
                info = request.form.get("add_video")
                if info == "":
                    status2 = "nothing"
                    return which4()
                else:
                    admin = open(filename,  "a")
                    admin.write(info + "\n")
                    admin.close()
                    return redirect(url_for('edit_workout'))
            case default:
                return which4()
def which4():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    filename = "Workout_videos.txt"
    exist = bool(path.exists(filename))
    if exist == False:
        create =  open(filename, "x")
        create.close()
    admin = open(filename, "r")
    adminvalue = admin.read().splitlines()
    admin.close()
    length3 = len(adminvalue)
    for i in range(0, len(names)):
        exist = bool(path.exists(names[i]))
        if exist == False:
            admin3 = open(names[i], "x")
            admin3.close()
    for i in range(0,len(names)):
        admin3 = open(names[i], "r")
        admin3value = admin3.read().splitlines()
        admin3.close()
        names2.append(admin3value)
    length2 = len(names2)
    match(status2):
        case "Load":
            return render_template("edit_workout.html", length2 = length2, groups = names2, names = names, length3 = length3 , videos = adminvalue )
        case "False_exist":
            return render_template("edit_workout.html", length2 = length2, groups = names2, names = names, stat = "Type in a valid file name!"
                                   , length3 = length3 , videos = adminvalue)
        case "nothing":
            return render_template("edit_workout.html", length2 = length2, groups = names2, names = names, stat = "Type in an input!",
                                   length3 = length3 , videos = adminvalue)
        case "number":
            return render_template("edit_workout.html", length2 = length2, groups = names2, names = names, stat = "Type in a number for line number!" ,
                                   length3 = length3 , videos = adminvalue)
        case "long":
            return render_template("edit_workout.html", length2 = length2, groups = names2, names = names, stat = "Line doesnt exist" ,
                                   length3 = length3 , videos = adminvalue)
        case default:
            return render_template("edit_workout.html", length2 = length2, groups = names2, names = names , length3 = length3 , videos = adminvalue)
        
def which3():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    filename = "food_videos.txt"
    exist = bool(path.exists(filename))
    if exist == False:
        create =  open(filename, "x")
        create.close()
    admin = open(filename, "r")
    adminvalue = admin.read().splitlines()
    admin.close()
    length3 = len(adminvalue)
    for i in range(0, len(names)):
        exist = bool(path.exists(names[i]))
        if exist == False:
            admin3 = open(names[i], "x")
            admin3.close()
    for i in range(0,len(names)):
        admin3 = open(names[i], "r")
        admin3value = admin3.read().splitlines()
        admin3.close()
        names2.append(admin3value)
    length2 = len(names2)
    match(status):
        case "Load":
            return render_template("edit_macro.html", length2 = length2, groups = names2, names = names, length3 = length3 , videos = adminvalue )
        case "False_exist":
            return render_template("edit_macro.html", length2 = length2, groups = names2, names = names, stat = "Type in a valid file name!"
                                   , length3 = length3 , videos = adminvalue)
        case "nothing":
            return render_template("edit_macro.html", length2 = length2, groups = names2, names = names, stat = "Type in an input!",
                                   length3 = length3 , videos = adminvalue)
        case "number":
            return render_template("edit_macro.html", length2 = length2, groups = names2, names = names, stat = "Type in a number for line number!" ,
                                   length3 = length3 , videos = adminvalue)
        case "long":
            return render_template("edit_macro.html", length2 = length2, groups = names2, names = names, stat = "Line doesnt exist" ,
                                   length3 = length3 , videos = adminvalue)
        case default:
            return render_template("edit_macro.html", length2 = length2, groups = names2, names = names , length3 = length3 , videos = adminvalue)
        
if __name__ == "__main__":
    app.run()
