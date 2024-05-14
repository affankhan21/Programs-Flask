from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/first")
def first():
    return render_template("first.html")
@app.route("/third")
def third():
    uname="AFFAN"
    lname="KHAN"
    company="zd"

    return render_template("third.html",uname=uname,lname=lname,company=company)

@app.route("/login")
def login():
    return render_template("login.html")
if(__name__=="__main__"):
    app.run(debug=True)
