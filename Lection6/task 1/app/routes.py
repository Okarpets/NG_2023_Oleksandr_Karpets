from app import app, db
from app.models import users
from flask import Flask, request, render_template, flash, get_flashed_messages, redirect, url_for, session
import sqlalchemy
from datetime import datetime
import os
from threading import Timer

##########################################################
#REGISTRATION-SESSION-EXIT SYSTEM
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        session['userlogged'] = "0" 
        session.pop('userlogged')  
        return render_template('index.html')
    else:
        uname = str(request.form['name']) 
        upassword = str(request.form['password']) 
        usession = str(request.form['repeat']) 
        if upassword == usession:
                if len(upassword) == 0 or len(uname) == 0 or len(usession) == 0:
                    flash("Invalid values")
                    return render_template('index.html')
                else:
                    try:
                        db.session.add(users(name = uname, password = upassword)) #Create a package from the data
                        db.session.commit()
                        session['userlogged'] = uname
                        flash("You have been registered")
                        return  redirect(url_for('send')) #Go to login to your account
                    except Exception:
                        flash("Sorry, this nickname is taken")
                        return render_template('index.html')
        else:
            flash("Password mismatch")
            return render_template('index.html')

###########################################################  
#LOGIN
@app.route('/send', methods=['POST','GET'])
def send():
    if request.method == 'GET':
        if 'userlogged' in session:
            uname = session['userlogged']
            return render_template('loggedsend.html', uname=uname)
        else:
            return render_template('send.html')
    else:


###########################################################              
#SELECT CHAT IF YOU ARE ALREADY LOGGED IN TO YOUR ACCOUNT

        if 'userlogged' in session: #IF THE USER HAS ALREADY BEEN LOGGED IN TO THE ACCOUNT AT LAST TIME
            uname = session['userlogged']
            session['chatname'] = "0"
            umessages = str(request.form['messages']) #SELECT A USER TO SEND TO
            if len(uname) == 0 or len(umessages) == 0:
                flash("Invalid values")
                return render_template('loggedsend.html', session=session, uname=uname)
            try:
                        #NEED TO CHECK THAT THE USER EXISTS
                        dbname = sqlalchemy.text("SELECT name FROM users WHERE name='{}'".format(umessages))
                        print(dbname)
                        checking = db.session.execute(dbname).all()
                        if str(checking) != "[('{0}',)]".format(umessages):
                                flash("This user doesn't exist")
                                return render_template('loggedsend.html', session=session, uname=uname)
                        else:
                                #CHECKING IF THERE IS A CHAT TABLE IN THE BASE
                                dbtabl = sqlalchemy.text("SELECT name FROM sqlite_master WHERE type='table'")
                                print(dbtabl)
                                tables = db.session.execute(dbtabl).all()
                                existcheck = 0
                                while (existcheck < len(tables)): 
                                    if str(tables[existcheck]) == ("('{0}{1}',)").format(uname, umessages) or str(tables[existcheck]) == ("('{0}{1}',)").format(umessages, uname):
                                        elem = str(tables[existcheck])
                                        chatname = elem[2:-3]
                                        session['chatname'] = chatname
                                        return redirect(url_for('all', session=session))
                                    existcheck += 1
                                chatmodel = sqlalchemy.text('''CREATE TABLE {0}{1} (
                                        name TEXT,
                                        messages TEXT,
                                        timemaneger TEXT)'''.format(uname, umessages))
                                print(chatmodel)
                                db.session.execute(chatmodel)
                                session['userlogged'] = uname
                                chatname = ("{0}{1}".format(uname,umessages))
                                session['chatname'] = chatname
                                return redirect(url_for('all', session=session)) #Go to login to your account
            except Exception:
                flash("DataBase error, please, try again")
                return render_template('loggedsend.html', session=session, uname=uname)
                    
###########################################################  
#LOGIN TO ACCOUNT

        else: # < If the user has never logged in before
            uname = str(request.form['namel']) #Get a nickname that you need to log in to
            upassword = str(request.form['passwordl']) #Account password 
        if len(upassword) == 0 or len(uname) == 0: #If the values ​​aren't correct - go back
                flash("Invalid values")
                return render_template('send.html')
        dbname = sqlalchemy.text("SELECT name FROM users WHERE name='{}'".format(uname))
        print(dbname)
        checking = db.session.execute(dbname).all()
        if str(checking) == "[('{0}',)]".format (uname): # < Comparing the name from the database with the FORMATTED one GIVEN BY THE USER
                dbpass = sqlalchemy.text("SELECT password FROM users WHERE name='{}'".format(uname)) #Search for password by username (uname)
                print(dbpass)
                dbpassword = db.session.execute(dbpass).one() #Get it from database
                if str(dbpassword) == ("('{0}',)".format(upassword)): # Comparing password
                        flash("You are logged")
                        session['userlogged'] = uname
                        return render_template('loggedsend.html', session=session, uname = session['userlogged'])
                else: 
                        flash("You forgot own password? :3, try to remember") #PASSWORD FAILED CHECKED
                        return render_template('send.html')
        else:
            flash("This username dosn't exist")
            return render_template('send.html')

###########################################################
#CHAT
@app.route('/all', methods=['POST','GET'])
def all():
    if request.method == 'GET':
        while True:
            uname = session['userlogged']
            chatname = session['chatname']
            other = chatname.replace(uname, "")
            sql = sqlalchemy.text("SELECT * FROM {}".format(chatname))
            print(sql)
            allchatuser = db.session.execute(sql).all()
            if allchatuser == []:
                    flash(("Now you don't have any messages")) #THIS USER DOESN'T HAVE ANY MESSAGES
                    return render_template('all.html',uname=uname, other=other)
            slicer = 0
            while slicer < len(allchatuser):
                        elem = str(allchatuser[slicer])
                        allchatuser[slicer] = elem[2:-2].replace("', '", " : ")
                        slicer += 1
            return render_template('all.html', uname=uname, chatname=chatname, allchatuser=allchatuser, other=other)
    else:
            uname = session['userlogged']
            chatname= session['chatname']
            send = str(request.form['sender'])
            other = chatname.replace(uname, "")
            now = datetime.now()
            timemaneger = ("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))
            if len(send) != 0:
                model = sqlalchemy.text('''INSERT INTO {} (name, messages, timemaneger) VALUES ('{}', '{}', '{}')'''.format(chatname, uname, send, timemaneger))
                db.session.execute(model)
                db.session.commit()
            sql = sqlalchemy.text("SELECT * FROM {}".format(chatname))
            print(sql)
            allchatuser = db.session.execute(sql).all()
            if allchatuser == []:
                    flash(("Now you don't have any messages")) #THIS USER DOESN'T HAVE ANY MESSAGES
                    return render_template('all.html',uname=uname, other=other)
            slicer = 0
            while slicer < len(allchatuser):
                        elem = str(allchatuser[slicer])
                        allchatuser[slicer] = elem[2:-2].replace("', '", " : ")
                        slicer += 1
            if len(send) == 0:
                flash("You can't send null string")
                return render_template('all.html', uname=uname, chatname=chatname, allchatuser=allchatuser, other=other)
            else:
                return render_template('all.html', uname=uname, chatname=chatname, allchatuser=allchatuser, other=other)
    