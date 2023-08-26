from flask import Flask, render_template,request,session,flash
import sqlite3 as sql
import os
import pandas as pd
from bs4 import BeautifulSoup as BS
import requests as req
from easygui import *
app = Flask(__name__)
with open('auto.txt', 'w') as fp:
    pass
with open('business.txt', 'w') as fp:
    pass
with open('sports.txt', 'w') as fp:
    pass
with open('test_g.txt', 'w') as fp:
    pass
with open('entertainment.txt', 'w') as fp:
    pass
with open('news1.txt', 'w') as fp:
    pass
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/gohome')
def homepage():
    return render_template('index.html')

@app.route('/service')
def servicepage():
    return render_template('services.html')

@app.route('/coconut')
def coconutpage():
    return render_template('Coconut.html')

@app.route('/cocoa')
def cocoapage():
    return render_template('cocoa.html')

@app.route('/arecanut')
def arecanutpage():
    return render_template('arecanut.html')

@app.route('/paddy')
def paddypage():
    return render_template('paddy.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')





@app.route('/enternew')
def new_user():
   return render_template('signup.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['Name']
            phonno = request.form['MobileNumber']
            email = request.form['email']
            unm = request.form['Username']
            passwd = request.form['password']
            with sql.connect("agricultureuser.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO agriuser(name,phono,email,username,password)VALUES(?, ?, ?, ?,?)",(nm,phonno,email,unm,passwd))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()

@app.route('/userlogin')
def user_login():
   return render_template("login.html")

@app.route('/logindetails',methods = ['POST', 'GET'])
def logindetails():
    if request.method=='POST':
            usrname=request.form['username']
            passwd = request.form['password']

            with sql.connect("agricultureuser.db") as con:
                cur = con.cursor()
                cur.execute("SELECT username,password FROM agriuser where username=? ",(usrname,))
                account = cur.fetchall()

                for row in account:
                    database_user = row[0]
                    database_password = row[1]
                    if database_user == usrname and database_password==passwd:
                        session['logged_in'] = True
                        return render_template('home.html')
                    else:
                        flash("Invalid user credentials")
                        return render_template('login.html')

@app.route('/predictinfo')
def predictin():
    url = "https://timesofindia.indiatimes.com/"

    webpage = req.get(url)
    trav = BS(webpage.content, "html.parser")
    M = 1
    for link in trav.find_all('a'):

        # PASTE THE CLASS TYPE THAT WE GET
        # FROM THE ABOVE CODE IN THIS AND
        # SET THE LIMIT GREATER THAN 35
        if (str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
            and len(link.string) > 35):
            print(str(M) + "\n", link.string)
            M += 1
            with open("news1.txt", "a", encoding='utf-8') as f:
                f.write("\n")
                f.write(link.string)
                
    title = "News"
    with open('news1.txt') as f:
        lines = f.read()

    # message for our window


    # button message by default it is "OK"
    button = "Close"

    # creating a message box
    msgbox(lines, title, button)
    M='News Generated'
    os.remove('news1.txt')

    return render_template('resultpred.html', prediction=M)

@app.route('/predictinfo1')
def predictin1():
    url = "https://timesofindia.indiatimes.com/business"

    webpage = req.get(url)
    trav = BS(webpage.content, "html.parser")
    M = 1
    for link in trav.find_all('a'):

        # PASTE THE CLASS TYPE THAT WE GET
        # FROM THE ABOVE CODE IN THIS AND
        # SET THE LIMIT GREATER THAN 35
        if (str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
            and len(link.string) > 35):
            print(str(M) + ".", link.string)
            M += 1
            with open("business.txt", "a", encoding='utf-8') as f:
                f.write("\n")
                f.write(link.string)
                

    title = "News"
    with open('business.txt') as f:
        lines = f.read()

    # message for our window


    # button message by default it is "OK"
    button = "Close"

    # creating a message box
    msgbox(lines, title, button)
    M='News Generated'
    os.remove('business.txt')

    return render_template('resultpred.html', prediction=M)
@app.route('/predictinfo2')
def predictin2():
    url = "https://timesofindia.indiatimes.com/etimes"

    webpage = req.get(url)
    trav = BS(webpage.content, "html.parser")
    M = 1
    for link in trav.find_all('a'):

        # PASTE THE CLASS TYPE THAT WE GET
        # FROM THE ABOVE CODE IN THIS AND
        # SET THE LIMIT GREATER THAN 35
        if (str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
            and len(link.string) > 35):
            print(str(M) + ".", link.string)
            M += 1
            with open("etimes.txt", "a", encoding='utf-8') as f:
                f.write("\n")
                f.write(link.string)
    title = "News"
    with open('etimes.txt', encoding='utf-8') as f:
        lines = f.read()

    # message for our window


    # button message by default it is "OK"
    button = "Close"

    # creating a message box
    msgbox(lines, title, button)
    M='News Generated'
    os.remove('etimes.txt')

    return render_template('resultpred.html', prediction=M)
@app.route('/predictinfo3')
def predictin3():
    # Sports
    url = "https://timesofindia.indiatimes.com/sports"

    webpage = req.get(url)
    trav = BS(webpage.content, "html.parser")
    M = 1
    for link in trav.find_all('a'):

        # PASTE THE CLASS TYPE THAT WE GET
        # FROM THE ABOVE CODE IN THIS AND
        # SET THE LIMIT GREATER THAN 35
        if (str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
            and len(link.string) > 35):
            print(str(M) + ".", link.string)
            M += 1
            with open("sports.txt", "a", encoding='utf-8') as f:
                f.write("\n")
                f.write(link.string)

    title = " Sports News"
    with open('sports.txt') as f:
        lines = f.read()

    # message for our window


    # button message by default it is "OK"
    button = "Close"

    # creating a message box
    msgbox(lines, title, button)
    M='News Generated'
    os.remove('sports.txt')

    return render_template('resultpred.html', prediction=M)
@app.route('/predictinfo4')
def predictin4():
    # Auto
    url = "https://timesofindia.indiatimes.com/auto"

    webpage = req.get(url)
    trav = BS(webpage.content, "html.parser")
    M = 1
    for link in trav.find_all('a'):

        # PASTE THE CLASS TYPE THAT WE GET
        # FROM THE ABOVE CODE IN THIS AND
        # SET THE LIMIT GREATER THAN 35
        if (str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
            and len(link.string) > 35):
            print(str(M) + ".", link.string)
            M += 1
            # Append-adds at last
            with open("auto.txt", "a", encoding='utf-8') as f:
                f.write("\n")
                f.write(link.string)
    title = "News"
    with open('auto.txt') as f:
        lines = f.read()

    # message for our window


    # button message by default it is "OK"
    button = "Close"

    # creating a message box
    msgbox(lines, title, button)
    M='News Generated'
    os.remove('auto.txt')

    return render_template('resultpred.html', prediction=M)



#return render_template('info.html')



@app.route('/predict',methods = ['POST', 'GET'])
def predcrop():
    if request.method == 'POST':
        comment = request.form['comment']
        print(comment)
        from GoogleNews import GoogleNews
        news = GoogleNews(period='1d')
        news.search(comment)
        result = news.result()
        import pandas as pd
        data = pd.DataFrame.from_dict(result)
        data = data.drop(columns=["img"])
        data.head()
        print(data)

        for i in result:
            # print("Title : ", i["title"])
            print("News : ", i["desc"])
            print("Read Full News : ", i["link"])
            with open("test_g.txt", "a") as myfile:
                myfile.write("\n\n")
                myfile.write(i["desc"])

        title = "News"
        with open('test_g.txt') as f:
            lines = f.read()

        # message for our window


        # button message by default it is "OK"
        button = "Close"

        # creating a message box
        msgbox(lines, title, button)
        M = 'News Generated'
        os.remove('test_g.txt')
    return render_template('resultpred.html', prediction=M)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('login.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

