from flask import Flask,render_template,redirect,make_response,request,session
import mysql.connector
app=Flask("__name__")
app.secret_key="1233"

DBHOST = 'localhost'
#DBNAME = 'assignment'
DBUSER = 'root'
DBPASS = ''
DBDATABASE="PlayerDB"
@app.route("/")
def showAllPlayers():
        con = mysql.connector.connect(host=DBHOST, user=DBUSER, passwd=DBPASS,database=DBDATABASE)
        sql="select * from player"
        cur=con.cursor()
        cur.execute(sql)
        players=cur.fetchall()
        con.close()
        return render_template("showAllPlayers.html",players=players)
@app.route("/addPlayer",methods=["GET","POST"])   
def addPlayer():
    if request.method=="GET":
        return render_template("addPlayer.html") 
    else:
        pname = request.form["pname"]
        age = request.form["age"]
        role = request.form["role"]
        runs = request.form["runs"]
        wickets = request.form["wickets"]
        matches = request.form["matches"]   
        con = mysql.connector.connect(host=DBHOST, user=DBUSER, passwd=DBPASS,database=DBDATABASE)
        sql="insert into player (pname,age,role,runs,wickets,matches) values(%s,%s,%s,%s,%s,%s)"
        val=(pname,age,role,runs,wickets,matches)
        cur=con.cursor()
        cur.execute(sql,val)
        con.commit()
        con.close()
        return redirect("/")



@app.route("/performAction",methods=["GET","POST"])
def performAction():
    if request.method == "POST":
        action = request.form["action"]
        pid = request.form["pid"]
        session["pid"]=pid
        if action == "Delete":
            return render_template("deleteConfirm.html")            
        else:
            pid= session["pid"]
            con = mysql.connector.connect(host=DBHOST, user=DBUSER, passwd=DBPASS,database=DBDATABASE)
            sql = "select * from Player where pid=%s"
            val = (pid,)
            cursor = con.cursor()
            cursor.execute(sql,val)
            record=cursor.fetchone()
            con.close()
            return render_template("edit.html",record=record)      
            
             
@app.route("/deleteConfirm",methods = ["GET","POST"])
def deleteConfirm():
    if request.method == "POST":
        pid = session["pid"]
        action = request.form["action"]
        if(action == "Yes"):
            con = mysql.connector.connect(host=DBHOST, user=DBUSER, passwd=DBPASS,database=DBDATABASE)
            sql = "delete from Player where pid=%s"
            val = (pid,)
            cursor = con.cursor()
            cursor.execute(sql,val)
            con.commit()
        return redirect("/")
      
                

@app.route("/editPlayer",methods = ["GET","POST"])
def editRecord():
        pid = session["pid"]
        if request.method == "POST":
            pname = request.form["pname"]
            age = request.form["age"]
            role = request.form["role"]
            runs = request.form["runs"]
            wickets = request.form["wickets"]
            matches = request.form["matches"] 
          
            con = mysql.connector.connect(host=DBHOST, user=DBUSER, passwd=DBPASS,database=DBDATABASE)
            sql = "update Player set pname=%s ,age=%s,role=%s ,runs=%s,wickets=%s ,matches=%s where pid=%s" 
            cursor = con.cursor()
            val=(pname,age,role,runs,wickets,matches,pid)
            cursor.execute(sql,val)
            con.commit()
            con.close()
        return redirect("/")
      
     
if(__name__=="__main__"):
    app.run(debug=True)