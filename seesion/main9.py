from flask import Flask,request,redirect,make_response,session,render_template
app=Flask(__name__)
app.secret_key="2108"
@app.route("/sessionDemo",methods=["GET","POST"])
def sessionDemo():
    if request.method == "GET":
        return render_template("sessionDemo.html")
    else:
        fname = request.form["fname"]
        lname = request.form["lname"]
        session["fname"] = fname
        session["lname"] = lname
        return "Session Created"
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login3.html")
    else:
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        if  uname =="Affan" and pwd=="Affan@21":
            session["uname"]=uname
            return redirect("/securedPage")
        else:
            return redirect("/login")    

@app.route("/securedPage")
def securedPage():
    if "uname" in session:
         uname=session["uname"]
         return render_template("securedPage.html",uname=uname)
    else:
        return redirect("/login")     



@app.route("/displaySession")
def displaySession():
    if "fname" in session:
        fname = session["name"]
        lname = session["lname"]
        return "Welcome "+fname+" "+lname
    else:
        return "Session not created"
if(__name__=="__main__"):
    app.run(debug=True)