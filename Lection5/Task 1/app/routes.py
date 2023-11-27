from app import app, db
from app.models import users, messages
from flask import Flask, request, render_template, flash, get_flashed_messages, redirect, url_for, session
import sqlalchemy

##########################################################
#REGISTRATION-SESSION-EXIT SYSTEM
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        session['userlogged'] = "0" # Log out of the session, 
        session.pop('userlogged')   # even if there isn't exist
        return render_template('index.html')
    else:
        uname = str(request.form['name']) #Get name of the user
        upassword = str(request.form['password']) #Get password of the user
        usession = str(request.form['repeat']) #Get password confirm of the user
        if upassword == usession:
                if len(upassword) == 0 or len(uname) == 0 or len(usession) == 0:
                    flash("Invalid values")
                    return render_template('index.html')
                else:
                    try: #We try to add a user, if there is no error
                        db.session.add(users(name = uname, password = upassword)) #Create a package from the data
                        db.session.commit()
                        session['userlogged'] = uname
                        flash("You have been registered")
                        return  redirect(url_for('all'))
                    except Exception: #We get error because it's username already exist
                        flash("Sorry, this nickname is taken")
                        return render_template('index.html')
        else:
            flash("Password mismatch")
            return render_template('index.html')


##########################################################
#LOGIN-SENDING SYSTEM
@app.route('/send', methods=['POST','GET'])
def send():
    if request.method == 'GET':
        if 'userlogged' in session:
            uname = session['userlogged']
            return render_template('loggedsend.html', uname=uname)
        else:
            return render_template('send.html')
    else:
        if 'userlogged' in session: #IF THE USER HAS ALREADY BEEN LOGGED IN TO THE ACCOUNT AT LAST TIME
            uname = session['userlogged'] #We knew username from session yet :3
            umessages = str(request.form['messages']) #GET ONLY MESSAGES ON THIS PROCCES
            if len(uname) == 0 or len(umessages) == 0:
                flash("Invalid values")
                return render_template('loggedsend.html', session=session, uname=uname)
            db.session.add(messages(user = uname, message = umessages)) #Sending messages to database
            db.session.commit()
            flash("We send your message")
            session['userlogged'] = uname
            return render_template('loggedsend.html', session=session, uname=uname) #Go back to SESSION EXIST page
        else: # < IF THE USER HAS NEVER LOGGED IN TO THE ACCOUNT BEFORE
            uname = str(request.form['namel']) #Get login nickname from the user
            upassword = str(request.form['passwordl']) #Get password from the user
            umessages = str(request.form['messages']) #Get password confirm of the user
        if len(upassword) == 0 or len(uname) == 0 or len(umessages) == 0:
                flash("Invalid values")
                return render_template('send.html')
        dbname = sqlalchemy.text("SELECT name FROM users WHERE name='{}'".format(uname))
        checking = db.session.execute(dbname).all()
        if str(checking) == "[('{0}',)]".format (uname): # < Comparing the name from the database with the FORMATTED one GIVEN BY THE USER
                dbpass = sqlalchemy.text("SELECT password FROM users WHERE name='{}'".format(uname)) #Search for password by username (uname)
                print(dbpass)
                dbpassword = db.session.execute(dbpass).one() #Get it from database
                if str(dbpassword) == ("('{0}',)".format (upassword)): # < Comparing the password from the database with the FORMATTED one GIVEN BY THE USER
                        db.session.add(messages(user = uname, message = umessages)) #Sending messages to database
                        db.session.commit()
                        flash("We send your message")
                        session['userlogged'] = uname
                        return render_template('loggedsend.html', session=session, uname = session['userlogged'])
                else: 
                        flash("You forgot own password? :3, try to remember") #PASSWORD FAILED CHECKED
                        return render_template('send.html')
        else:
            flash("This username dosn't exist") #THIS USER DOESN'T EXISTS IN THE DATABASE
            return render_template('send.html')

@app.route('/all', methods=['POST','GET'])
def all():
    if request.method == 'GET':
        uname = session['userlogged']
        return render_template('all.html',uname=uname)
    else:
        uname = session['userlogged']
        sql = sqlalchemy.text("SELECT message FROM messages WHERE user='{}'".format(uname))
        print(sql)
        allusermsg = db.session.execute(sql).all()
        if allusermsg == []:
                flash(("Now you don't have any messages")) #THIS USER DOESN'T HAVE ANY MESSAGES
                return render_template('all.html', uname=uname)
        else:
            slicer = 0
            while slicer < len(allusermsg):
                    elem = str(allusermsg[slicer])
                    allusermsg[slicer] = elem[2:-3]
                    slicer += 1
        return render_template('all.html',  allusermsg=allusermsg, uname=uname)