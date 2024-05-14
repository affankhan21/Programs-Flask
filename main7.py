from flask import Flask,render_template,make_response,request
from datetime import datetime,timedelta
app=Flask(__name__)
@app.route("/cookieDemo",methods=["GET","POST"])
def cookieDemo():
    if request.method=="GET":
        return render_template("cookieDemo.html")
    else:
        fname = request.form["fname"]
        lname = request.form["lname"]
        bname = request.form["bname"]
        action = request.form["action"]
        resp = make_response(render_template("welcomecookie.html"))    
        
        resp.set_cookie("fname",fname)
        resp.set_cookie("lname",lname)
        resp.set_cookie("bname",bname)

        return resp

@app.route("/displayCookie")
def getCookie():
    fname = request.cookies.get("fname")
    lname = request.cookies.get("lname")
    uname = fname+" "+lname
    return "Hello " + uname        
if(__name__=="__main__"):
    app.run(debug=True)