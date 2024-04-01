import os
from flask import Flask, session, render_template, request, redirect,url_for, flash, jsonify
from flask_session import Session
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from models import *
from werkzeug.utils import secure_filename
from datetime import datetime
import qrcode
from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib.pyplot
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

mail = Mail(app)
s = URLSafeTimedSerializer('Thisisasecret!')

# Configure session to use filesystem
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost/qrconnect"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def login():
    if session.get("username") == None:
        return render_template("login.html")
    else:
        if session.get("user_type") == "mentee":
            return redirect(url_for('menteeHome'))
        else:
            return redirect(url_for('mentorHome'))


@app.route("/validateUser", methods=["POST"])
def validateUser():
    username = request.form.get("username")
    password = request.form.get("password")
    try:
        user_data = Mentee.query.filter_by(username=username).one()
    except:
        #username not in the mentee table try the mentor table
        try:
            user_data = Mentor.query.filter_by(username=username).one()
        except:
            #not in the mentor or mentee table
            flash("Error: Username does not exist")
            return redirect(url_for('login'))
        else:
            user_data_fetched = True
            user_type = "mentor"
    else:
        user_data_fetched = True
        user_type = "mentee"

    if user_data_fetched:
        if password == user_data.password:
            file_path = "img/" + str(user_data.profile_pic)
            session.update({"username":username, "fname":user_data.fname, "lname":user_data.lname,"user_type":user_type,"email":user_data.email, "pic":file_path, "cv_help":user_data.cv_help, "bio":user_data.bio ,"mockInterview":user_data.mockInterview })
            if user_type == "mentee":
                file_path = "img/" + str(user_data.profile_pic)
                session.update({"username": user_data.username, "meetAlumni": user_data.meetAlumni, "fname":user_data.fname, "lname":user_data.lname, "dob": user_data.dob, "year": user_data.year, "email": user_data.email, "mobile_no": user_data.mobile_no, "address": user_data.address, "blood_grp": user_data.blood_grp, "father_name": user_data.father_name, "father_occupation": user_data.father_occupation, "father_email": user_data.father_email, "father_mobile_no": user_data.father_mobile_no, "mother_name": user_data.mother_name, "mother_occupation": user_data.mother_occupation, "mother_email": user_data.mother_email, "mother_mobile_no": user_data.mother_mobile_no, "hobbies": user_data.hobbies, "strengths": user_data.strengths, "weakness": user_data.weakness, "goals": user_data.goals, "ssc": user_data.ssc, "hsc": user_data.hsc, "cet_jee": user_data.cet_jee, "bio": user_data.bio, "prn_num": user_data.prn_num, "branch": user_data.branch, "batch": user_data.batch, "linkedin_pro": user_data.linkedin_pro})
                return redirect(url_for('menteeHome'))
            else:
                session.update({"job":user_data.job, "meetStudents":user_data.meetStudents, "workExp":user_data.workExp})
                return redirect(url_for('mentorHome'))
        else:
            flash("Error: Incorrect password or username, please try again!")
            return redirect(url_for('login'))


@app.route('/log_out')
def log_out():
    session.pop("username")
    return redirect(url_for('login'))


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/editProfile", methods=["GET", "POST"])
def editProfile():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session.get('username')
    user_type = session.get('user_type')

    if user_type == 'mentor':
        mentor = Mentor.query.filter_by(username=username).first()

        if request.method == "POST":
            # Handle mentor profile update here
            mentor.fname = request.form.get("fname")
            mentor.lname = request.form.get("lname")
            mentor.email = request.form.get("email")
            mentor.job = request.form.get("job")
            mentor.cv_help = True if request.form.get("cvhelp") == "on" else False
            mentor.meet_students = True if request.form.get("meet_students") == "on" else False
            mentor.mockInterview = True if request.form.get("mockInterview") == "on" else False
            mentor.workExp = True if request.form.get("workExp") == "on" else False

            # Add more fields as needed

            db.session.commit()
            return redirect(url_for('mentorHome'))

        return render_template("editProfile.html", mentor=mentor)

    elif user_type == 'mentee':
        mentee = Mentee.query.filter_by(username=username).first()

        if request.method == "POST":
            # Handle mentee profile update here
            mentee.fname = request.form.get("fname")
            mentee.lname = request.form.get("lname")
            mentee.email = request.form.get("email")
            mentee.prn_num = request.form.get("prn_num")
            mentee.dob = request.form.get("dob")
            mentee.year = request.form.get("year")
            mentee.mobile_no = request.form.get("mobile_no")
            mentee.address = request.form.get("address")
            mentee.blood_grp = request.form.get("blood_grp")
            mentee.branch = request.form.get("branch")
            mentee.batch = request.form.get("batch")
            mentee.linkedin_pro = request.form.get("linkedin_pro")
            mentee.father_name = request.form.get("father_name")
            mentee.father_occupation = request.form.get("father_occupation")
            mentee.father_mobile_no = request.form.get("father_mobile_no")
            mentee.father_email = request.form.get("father_email")
            mentee.mother_name = request.form.get("mother_name")
            mentee.mother_occupation = request.form.get("mother_occupation")
            mentee.mother_mobile_no = request.form.get("mother_mobile_no")
            mentee.mother_email = request.form.get("mother_email")
            mentee.hobbies = request.form.get("hobbies")
            mentee.strengths = request.form.get("strengths")
            mentee.weakness = request.form.get("weakness")
            mentee.goals = request.form.get("goals")
            mentee.ssc = request.form.get("ssc")
            mentee.hsc = request.form.get("hsc")
            mentee.cet_jee = request.form.get("cet_jee")
            mentee.cv_help = True if request.form.get("cvhelp") == "on" else False
            mentee.meetAlumni = True if request.form.get("meetAlumni") == "on" else False
            mentee.mockInterview = True if request.form.get("mockInterview") == "on" else False

            # Add more fields as needed

            db.session.commit()
            return redirect(url_for('menteeHome'))
        
        academic_record = Mentee_Grades.query.filter_by(username=username)
        return render_template("editProfile.html", mentee=mentee, academic_record=academic_record)

    else:
        # Handle other user types or unexpected cases
        return redirect(url_for('home'))
        

@app.route("/registerUser", methods=["POST"])
def registerUser():
    menteeForm = request.form.get("menteeFormbutton")
    mentorForm = request.form.get("mentorFormButton")

    print(" ---------------- in the register user function ---------------- ----------------")

    if mentorForm != None:
        fname = request.form.get("fname2")
        lname = request.form.get("lname2")
        username = request.form.get("username2")
        password = request.form.get("password2")
        email = request.form.get("email")
        job = request.form.get("job")

        cv_help = True if request.form.get("cvhelp2") == "on" else False
        meet_students = True if request.form.get("meet_students") == "on" else False
        mockInterview = True if request.form.get("mockInterview2")  == "on" else False
        workExp = True if request.form.get("workExp") == "on" else False
        
        existing_mentor = Mentor.query.filter_by(username=username).first()
        
        if existing_mentor:
            flash("Error: Username already exists. Please choose a different username.")
            return redirect(url_for('register'))
        
        if not (8 <= len(password) <= 20 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
            flash("Error: Password must be 8-20 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
            return redirect(url_for('register'))
        
        new_mentor = Mentor(fname=fname, lname=lname, username=username, profile_pic= "mentor_pic.png" ,password=password, email=email, job=job, cv_help=cv_help, meetStudents= meet_students, mockInterview=mockInterview, workExp=workExp)
        db.session.add(new_mentor)
        db.session.commit()
        session.update({"username":username, "fname":fname, "lname":lname, "bio":"-", "pic":"img/mentor_pic.png" , "user_type":"mentor", "email":email, "job":job, "cv_help":cv_help,"meetStudents":meet_students, "mockInterview":mockInterview, "workExp":workExp })
        
    else:
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        prn_num = request.form.get("prn_num")
        dob = request.form.get("dob")
        year = request.form.get("")
        mobile_no = request.form.get("")
        address = request.form.get("")
        blood_grp = request.form.get("")
        branch = request.form.get("")
        batch = request.form.get("")
        linkedin_pro = request.form.get("")
        father_name = request.form.get("")
        father_occupation = request.form.get("")
        father_mobile_no = request.form.get("")
        father_email = request.form.get("")
        mother_name = request.form.get("")
        mother_occupation = request.form.get("")
        mother_mobile_no = request.form.get("")
        mother_email = request.form.get("")
        hobbies = request.form.get("")
        strengths = request.form.get("")
        weakness = request.form.get("")
        goals = request.form.get("")
        ssc = request.form.get("")
        hsc = request.form.get("")
        cet_jee = request.form.get("")

        cv_help = True if request.form.get("cvhelp") == "on" else False
        meetAlumni = True if request.form.get("meetAlumni") == "on" else False
        mockInterview = True if request.form.get("mockInterview") == "on" else False
        
        existing_mentee = Mentee.query.filter_by(username=username).first()
    
        if existing_mentee:
            flash("Error: Username already exists. Please choose a different username.")
            return redirect(url_for('register'))
    
        if not (8 <= len(password) <= 20 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
            flash("Password must be 8-20 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
            return redirect(url_for('register'))
        
        new_mentee = Mentee(fname=fname, lname=lname, prn_num = "", year = '', branch = "", batch = "",username=username, profile_pic= "mentee_pic.png" , password=password, linkedin_pro = "", dob = "", mobile_no = "", address = '', blood_grp = '', father_name = '', father_occupation = '', father_mobile_no = '', father_email = '', mother_name = '', mother_occupation = '', mother_mobile_no = '', mother_email = '', ssc = '', hsc = '', cet_jee = '', hobbies = '', strengths = '', weakness = '', goals = '', email=email, cv_help=cv_help, meetAlumni= meetAlumni, mockInterview=mockInterview)
        db.session.add(new_mentee)
        db.session.commit()
        session.update({"username":username, "fname":fname, "lname":lname, 'prn_num': prn_num, 'dob': dob, 'mobile_no': mobile_no, 'address': address, 'blood_grp': blood_grp, 'father_name': father_name, 'father_occupation': father_occupation, 'father_mobile_no': father_mobile_no, 'father_email': father_email, 'mother_name': mother_name, 'mother_occupation': mother_occupation, 'mother_mobile_no': mother_mobile_no, 'mother_email': mother_email, 'hobbies': hobbies, 'strengths': strengths, 'weakness': weakness, 'goals': goals, 'ssc': ssc, 'hsc': hsc, 'cet_jee': cet_jee,"bio":"-", "pic":"img/mentee_profile.png", "user_type":"mentee", 'year': year, "email":email, "branch": branch, "batch": batch, "linkedin_pro": linkedin_pro,"cv_help":cv_help,"meetAlumni": meetAlumni, "mockInterview":mockInterview})
        
    email = request.form['email']
    token = s.dumps(email, salt='email-confirm')
    
    msg = Message('Confirm Email', sender='dhruvshetty2502@gmail.com', recipients=[email])
    
    link = url_for('confirm_email', token=token, _external=True)

    # Modify the body to include the link with target="_blank"
    html_content = '<html><body>Click <a href="{}" target="_blank">here</a> to confirm your email address.</body></html>'.format(link)

    # Set the HTML content for the message
    msg.html = html_content

    # Send the message
    mail.send(msg)
            
    return render_template('verify.html', email=email)


@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        user_type = session.get('user_type')
        # Determine the appropriate model based on user_type
        if user_type == 'mentor':
            user = Mentor.query.filter_by(email=email).first()
        elif user_type == 'mentee':
            user = Mentee.query.filter_by(email=email).first()
        else:
            return '<h1>Invalid user type!</h1>'

        if user:
            # Update the user's email_verified field
            user.email_verified = True
            # Commit changes to the database
            db.session.commit()
            return render_template('email_verified.html')
        else:
            # Handle case where user is not found
            return '<h1>User not found!</h1>'
    except:
        return '<h1>Token expired!!</h1>'


@app.route("/menteeHome", methods=["GET"])
def menteeHome():
    return render_template("menteeHome.html")


@app.route("/mentorHome", methods=["GET"])
def mentorHome():
    #add a check to make sure that the user is indeed a mentor
    return render_template("mentorHome.html")


@app.route("/resources", methods=["GET"])
def resources():
    username = session.get('username')
    resources_data = Resource.query.filter_by(username=username).all()
    NUMBER_OF_RESOURCES = len(resources_data)
    return render_template("resources.html", resources_data = resources_data)


@app.route("/deleteResource/<int:id>", methods=["POST"])
def deleteResource(id):
    # Fetch the resource by its ID and delete it
    resource = Resource.query.get(id)
    if resource:
        db.session.delete(resource)
        db.session.commit()
    return redirect(url_for('resources'))


@app.route("/network", methods=["GET", "POST"])
def network():
    mentee_data = session["mentee_data"] = True
    mentor_data = session["mentor_data"] = True
    if request.method == 'POST':
        mentee_data = session["mentee_data"] = True if request.form.get("viewMentees") == "on" else False
        mentor_data = session["mentor_data"] = True if request.form.get("viewMentors") == "on" else False
    if mentee_data:
        mentee_data = Mentee.query.filter_by().all()
    if mentor_data:
        mentor_data = Mentor.query.filter_by().all()
    if (not mentee_data) and (not mentor_data):
        flash("I hope you enjoy looking at a blank screen...")
    return render_template("network.html",  mentee_data = mentee_data, mentor_data = mentor_data)


@app.route('/changePassword', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        username = session.get('username')
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')

        # Query the Mentee table for the specific user
        mentee = Mentee.query.filter_by(username=username).first()

        if mentee:
            if mentee.password == old_password:
                # The old password is correct, update the password for the user
                mentee.password = new_password
                db.session.commit()
                flash('Password successfully changed')
                return redirect(url_for('editProfile'))
            else:
                flash('Error: Old password is incorrect')
        
    # Render the "Change Password" page for GET requests
    return render_template('change_password.html')


@app.route('/deleteMentee/<username>', methods=['GET', 'POST'])
def delete_mentee(username):
    # Handle the deletion of the mentee with the given username
    mentee = Assigned_Mentee.query.filter_by(mentee=username).first()

    if mentee:
        # Delete the mentee from your database
        db.session.delete(mentee)
        db.session.commit()
        flash(f'Mentee {username} has been deleted', 'success')
    else:
        flash(f'Mentee {username} not found', 'error')

    return redirect(url_for('mentee'))


@app.route("/profileChanges", methods=["POST"])
def profileChanges():
    if session.get("user_type") == "mentee":
        user_data = Mentee.query.filter_by(username=session.get("username")).one()
        user_data.meetAlumni = session["meetAlumni"] = True if request.form.get("meetAlumni") == "on" else False
        user_data.mockInterview = session["mockInterview"] = True if request.form.get("mockInterview") == "on" else False
        
        user_data.fname = session["fname"] = request.form.get("fname")
        user_data.lname = session["lname"] = request.form.get("lname")
        user_data.prn_num = session["prn_num"] = request.form.get("prn_num")
        user_data.dob = session["dob"] = request.form.get("dob")
        user_data.year = session["year"] = request.form.get("year")
        user_data.mobile_no = session["mobile_no"] = request.form.get("mobile_no")
        user_data.address = session["address"] = request.form.get("address")
        user_data.blood_grp = session["blood_grp"] = request.form.get("blood_grp")
        user_data.branch = session["branch"] = request.form.get("branch")
        user_data.batch = session["batch"] = request.form.get("batch")
        user_data.father_name = session["father_name"] = request.form.get("father_name")
        user_data.father_occupation = session["father_occupation"] = request.form.get("father_occupation")
        user_data.father_mobile_no = session["father_mobile_no"] = request.form.get("father_mobile_no")
        user_data.father_email = session["father_email"] = request.form.get("father_email")
        user_data.mother_name = session["mother_name"] = request.form.get("mother_name")
        user_data.mother_occupation = session["mother_occupation"] = request.form.get("mother_occupation")
        user_data.mother_mobile_no = session["mother_mobile_no"] = request.form.get("mother_mobile_no")
        user_data.mother_email = session["mother_email"] = request.form.get("mother_email")
        user_data.hobbies = session["hobbies"] = request.form.get("hobbies")
        user_data.strengths = session["strengths"] = request.form.get("strengths")
        user_data.weakness = session["weakness"] = request.form.get("weakness")
        user_data.goals = session["goals"] = request.form.get("goals")
        user_data.ssc = session["ssc"] = request.form.get("ssc")
        user_data.hsc = session["hsc"] = request.form.get("hsc")
        user_data.cet_jee = session["cet_jee"] = request.form.get("cet_jee")
        user_data.linkedin_pro = session["linkedin_pro"] = request.form.get("linkedin_pro")        
    else:
        user_data = Mentor.query.filter_by(username=session.get("username")).one()
        user_data.meetStudents = session["meetStudents"] = True if request.form.get("meet_students") == "on" else False
        user_data.mockInterview = session["mockInterview"] = True if request.form.get("mockInterview2") == "on" else False
        user_data.workExp = session["workExp"] = True if request.form.get("workExp") == "on" else False
    
        user_data.job = session["job"] = request.form.get("job")
        user_data.bio = session["bio"] = request.form.get("bio")
        user_data.cv_help = session["cv_help"] = True if request.form.get("cvhelp2") == "on" else False
        
    file = request.files['file'] #this gets the file
    if not file.filename == '':
        filename = secure_filename(file.filename)
        picture_path = os.path.join(app.root_path, 'static/img', filename)
        print(picture_path)
        file.save(picture_path)
        user_data.profile_pic = filename
        session["pic"] = "img/" + str(filename)
        flash("Profile picture has been uploaded")
    
    username = session.get('username')
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=15, border=5)
    filename = f"static/img/qrcode_{session['username']}.png"
    profile_data = f'http://127.0.0.1:5000//verify_mentor_credentials/{username}'
    qr.add_data(profile_data)
    qr.make(fit=True)

    # Create an image of the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(filename)
    
    timestamp = int(datetime.now().timestamp())
    db.session.commit()
    
    if session["bio"] == "":
        flash("Adding a bio will make your profile look good! (Changes of any other fields have been saved)")
        return redirect(url_for('editProfile'))
    flash("Changes have been saved to the database")
    return render_template("editProfile.html", timestamp=timestamp)


@app.route('/view_profile/<username>', methods=['GET', 'POST'])
def view_profile(username):
    mentee = Mentee.query.filter_by(username=username).first()
    return render_template('viewProfile.html', mentee=mentee)


@app.route('/verify_mentor_credentials/<username>', methods=['GET', 'POST'])
def verify_mentor_credentials(username):
    mentee_username = username
    if request.method == 'POST':
        mentor_username = request.form.get('mentor_username')
        mentor_password = request.form.get('mentor_password')
        
        # Check if mentor exists in the database with the provided credentials
        mentor = Mentor.query.filter_by(username=mentor_username, password=mentor_password).first()
        
        if mentor:
            # Get the mentee and mentor usernames and update the assigned_mentees table
            mentor_username = mentor.username

            try:# Update the assigned_mentees table
                assignment = Assigned_Mentee(mentee=mentee_username, mentor=mentor_username)
                db.session.add(assignment)
                db.session.commit()
                return redirect(url_for('view_profile', username=mentee_username))
            except Exception as e:
                flash("Error: Mentor already assigned to mentee")
        else:
            flash("Error: Invalid mentor credentials.")
    
    return render_template('mentor_credentials_prompt.html')


@app.route("/academicChanges", methods=["POST"])
def academicChanges():
    if session.get("user_type") == "mentee":
        try:
            username = session.get('username')
            
            # Retrieve the total number of rows from the form
            total_rows = int(request.form.get('row-count'))
            all_rows_filled = True
            user_data_list = []

            # Iterate through the rows and collect data
            for i in range(total_rows):
                sem = request.form.get('sem')
                subject = request.form.get(f'subject_{i}')
                marks_ia = request.form.get(f'marks_ia_{i}')
                marks_sem = request.form.get(f'marks_sem_{i}')
                total_marks = request.form.get(f'total_marks_{i}')
                cgpa = request.form.get('cgpa')
                
                # Check if any of the fields in the row are empty
                if not subject or not marks_ia or not marks_sem or not total_marks:
                    all_rows_filled = False
                    flash("Error: Please fill in all fields for each row.")
                    break  # Exit the loop if any row is incomplete

                # Create a dictionary for each row's data
                user_data = {
                    'username': username,
                    'sem': sem,
                    'subject': subject,
                    'marks_ia': marks_ia,
                    'marks_sem': marks_sem,
                    'total_marks': total_marks,
                    'cgpa': cgpa
                }
                user_data_list.append(user_data)

            if all_rows_filled:
                # Delete existing entries for the given semester and user
                for data in user_data_list:
                    Mentee_Grades.query.filter_by(username=data['username'], sem=data['sem']).delete()

                # Create new entries
                for data in user_data_list:
                    new_entry = Mentee_Grades(**data)
                    db.session.add(new_entry)

                # Commit changes to the database
                db.session.commit()
                flash("Grades have been added!")
        except Exception as e:
            flash("Error: An error occurred while processing form data: " + str(e))
            db.session.rollback()  # Rollback changes if an error occurs
    else:
        flash("Error: User is not a mentee")

    return redirect(url_for('editProfile'))


@app.route('/mentee', methods=['GET'])
def mentee():
    mentor_username = session.get('username')  # Get the mentor's username from the session

    # Fetch the usernames of mentees assigned to the mentor
    mentee_usernames = [record.mentee for record in Assigned_Mentee.query.with_entities(Assigned_Mentee.mentee)]
    
    # Fetch all records from the assigned_mentees table for the specific mentor
    assigned_mentees = Assigned_Mentee.query.filter_by(mentor=mentor_username).all()
    
    mentee_names = [mentee.mentee for mentee in assigned_mentees]
    
    academic_details = Mentee_Grades.query.filter(Mentee_Grades.username.in_(mentee_usernames)).all()
    # Fetch resources corresponding to the mentees in the mentee_usernames list
    resources_data = Resource.query.filter(Resource.username.in_(mentee_usernames)).all()

    return render_template('mentee.html', mentees=mentee_names, resources_data=resources_data, academic_details=academic_details)


@app.route("/addResource", methods=["POST"])
def addResource():
    username = session.get('username')
    title = request.form.get("resource_title")
    description = request.form.get("resource_description")
    file = request.files['file']  # this gets the file
    date_uploaded = datetime.utcnow()  # Get the current date and time

    # Define the target directory for saving files
    target_dir = os.path.join(app.root_path, 'static', 'resources')

    # Ensure the target directory exists, and create it if it doesn't
    os.makedirs(target_dir, exist_ok=True)

    # Check if a file was selected
    if not file.filename == '':
        filename = secure_filename(file.filename)
        resource_path = os.path.join(target_dir, filename)
        file.save(resource_path)
    else:
        # If they haven't added a resource, flash them a message
        flash("Error: Please select a file to add as a resource")
        return redirect(url_for('resources'))

    NUMBER_OF_RESOURCES = len(Resource.query.filter_by().all())
    new_resource = Resource(id=NUMBER_OF_RESOURCES + 1, username=username, title=title, description=description, file=filename, date_uploaded=date_uploaded)
    db.session.add(new_resource)
    db.session.commit()
    flash("Resource has been added!")
    return redirect(url_for('resources'))


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        
        # Check if the email exists in the Mentee or Mentor table
        if Mentee.query.filter_by(email=email).first() or Mentor.query.filter_by(email=email).first():
            token = s.dumps(email, salt='email-confirm')
            
            msg = Message('Reset Password', sender='your_email@gmail.com', recipients=[email])
            
            link = url_for('reset_password', token=token, _external=True)

            # Modify the body to include the link with target="_blank"
            html_content = '<html><body>Click <a href="{}" target="_blank">here</a> to reset your password.</body></html>'.format(link)

            # Set the HTML content for the message
            msg.html = html_content

            # Send the message
            mail.send(msg)
                    
            flash('Password reset email sent successfully!')
            return redirect(url_for('forgot_password'))
        else:
            flash('Error: Email not found!')
            return redirect(url_for('forgot_password'))
    return render_template('forgot_password.html')


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if request.method == 'GET':
        try:
            email = s.loads(token, salt='email-confirm', max_age=3600)  # Max age for the token: 1 hour
            return render_template('reset_password.html', email=email)
        except:
            flash('Error: The link is invalid or expired.')
            return redirect(url_for('forgot_password'))
    else:
        # Handle password reset logic here
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        
        if new_password != confirm_password:
            flash('Error: Passwords do not match!')
            return redirect(url_for('reset_password', token=token))
        else:
            try:
                email = s.loads(token, salt='email-confirm', max_age=3600)
                user = Mentee.query.filter_by(email=email).first()
                if user:
                    # Update the user's password
                    user.password = confirm_password
                    db.session.commit()
                    
                    flash('Password reset successful!')
                    return redirect(url_for('login'))  # Redirect to login page after successful password reset
                else:
                    flash('Error: User not found!')
                    return redirect(url_for('forgot_password'))
            except:
                flash('Error: The link is invalid or expired.')
                return redirect(url_for('forgot_password'))


@app.route("/analysis", methods=["GET", "POST"])
def analysis():
    username = session.get('username')

    # SQL query to retrieve CGPA for the logged-in mentee
    query = f"SELECT MIN(cgpa) as cgpa FROM mentee_grades WHERE username = '{username}' GROUP BY sem ORDER BY sem"
    
    # Retrieve data from SQL database into a Pandas DataFrame
    df = pd.read_sql(query, app.config["SQLALCHEMY_DATABASE_URI"])
    
    # Plot data
    plt.plot(range(1, len(df) + 1), df['cgpa'], marker='o', color='b', linestyle='-')

    # Add labels and title
    plt.xlabel('Semester')
    plt.ylabel('CGPA (out of 10)')
    plt.title('Mentee CGPA Progress')

    plt.xticks(range(1, len(df) + 1))  # Set x-axis ticks to match semester numbers
    plt.yticks(range(12))

    for i, cgpa in enumerate(df['cgpa']):
       plt.annotate(f'CGPA: {cgpa:.2f}', (i + 1, cgpa), textcoords="offset points", xytext=(0,10), ha='center')
    
    # Convert plot to base64-encoded image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode()

    # Close plot to free up resources
    plt.close()
    
    if request.method == "POST":
        # Retrieve selected semester from the form
        selected_semester = request.form.get("semester")

        # Query the database for subject contributions for the selected semester
        query = f"SELECT subject, total_marks FROM mentee_grades WHERE username = '{username}' and sem = '{selected_semester}'"
        df = pd.read_sql(query, app.config["SQLALCHEMY_DATABASE_URI"])

        # Calculate the contribution of each subject based on the total marks
        total_marks_semester = df['total_marks'].sum()
        subject_contributions = df.groupby('subject')['total_marks'].sum() / total_marks_semester

        # Plot the data as a pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(subject_contributions, labels=subject_contributions.index, autopct='%1.1f%%', startangle=140)
        plt.title(f'Contribution of Subjects in Semester {selected_semester}')

        # Convert plot to base64-encoded image
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data1 = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        query = f"SELECT subject, marks_ia, marks_sem FROM mentee_grades WHERE username = '{username}' and sem = '{selected_semester}'"

        # Retrieve data from SQL database into a Pandas DataFrame
        df = pd.read_sql(query, app.config["SQLALCHEMY_DATABASE_URI"])

        # Plot data
        plt.figure(figsize=(12, 6))

        # Set the width of the bars
        bar_width = 0.35

        # Set the positions of the bars on the x-axis
        index = np.arange(len(df))

        # Plot bars for internal assessment marks
        plt.bar(index, df['marks_ia'], bar_width, label='Internal Assessment Marks')

        # Plot bars for semester marks
        plt.bar(index + bar_width, df['marks_sem'], bar_width, label='Semester Marks')

        # Add labels and title
        plt.xlabel('Subjects')
        plt.ylabel('Marks')
        plt.title(f'Comparison of Internal Assessment Marks and Semester Marks for Semester {selected_semester}')
        plt.xticks(index + bar_width / 2, df['subject'])
        plt.legend()

        # Set the upper limit on the y-axis
        plt.ylim(0, 80)

        # Customize plot (optional)
        plt.grid(True, axis='y')

        # Convert plot to base64-encoded image
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data3 = base64.b64encode(buffer.read()).decode()

        # Close plot to free up resources
        plt.close()

        return render_template('analysis.html', plot_data=plot_data, initial_plot_data=plot_data1, plot_data3=plot_data3, selected_semester=selected_semester)

    else:
        selected_semester = request.form.get("semester")
        # Render the page with the initial pie chart data for the first semester
        # Query the database for subject contributions for the first semester
        query = f"SELECT subject, total_marks FROM mentee_grades WHERE username = '{username}' and sem = '1'"
        df = pd.read_sql(query, app.config["SQLALCHEMY_DATABASE_URI"])

        # Calculate the contribution of each subject based on the total marks
        total_marks_semester = df['total_marks'].sum()
        subject_contributions = df.groupby('subject')['total_marks'].sum() / total_marks_semester

        # Plot the data as a pie chart
        plt.figure(figsize=(8, 8))
        plt.pie(subject_contributions, labels=subject_contributions.index, autopct='%1.1f%%', startangle=140)
        plt.title('Contribution of Subjects in Semester 1')

        # Convert plot to base64-encoded image
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        initial_plot_data = base64.b64encode(buffer.read()).decode()
        plt.close()
        
        query = f"SELECT subject, marks_ia, marks_sem FROM mentee_grades WHERE username = '{username}' and sem = '1'"

        # Retrieve data from SQL database into a Pandas DataFrame
        df = pd.read_sql(query, app.config["SQLALCHEMY_DATABASE_URI"])

        # Plot data
        plt.figure(figsize=(12, 6))

        # Set the width of the bars
        bar_width = 0.35

        # Set the positions of the bars on the x-axis
        index = np.arange(len(df))

        # Plot bars for internal assessment marks
        plt.bar(index, df['marks_ia'], bar_width, label='Internal Assessment Marks')

        # Plot bars for semester marks
        plt.bar(index + bar_width, df['marks_sem'], bar_width, label='Semester Marks')

        # Add labels and title
        plt.xlabel('Subjects')
        plt.ylabel('Marks')
        plt.title(f'Comparison of Internal Assessment Marks and Semester Marks for Semester 1')
        plt.xticks(index + bar_width / 2, df['subject'])
        plt.legend()

        # Set the upper limit on the y-axis
        plt.ylim(0, 80)

        # Customize plot (optional)
        plt.grid(True, axis='y')

        # Convert plot to base64-encoded image
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_data3 = base64.b64encode(buffer.read()).decode()

        # Close plot to free up resources
        plt.close()
        
        return render_template('analysis.html', plot_data=plot_data, initial_plot_data=initial_plot_data, plot_data3=plot_data3, selected_semester=selected_semester)