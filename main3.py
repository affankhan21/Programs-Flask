from flask import Flask,render_template,request 
app=Flask("__name__")


@app.route("/mydict")
def mydict():
    data={101:"affan",102:"zain",103:"rahil"}
    return render_template("mydict.html",data=data)
@app.route("/login1")    
def login():
    return render_template("login2.html")
@app.route("/verify",methods=["POST"])
def verify():
    uname=request.form["uname"]
    pwd=request.form["password"]
    if( uname=="Affan" and pwd=="Affan@21"):
        return "Success"
    else:
        return "Failed"    
if(__name__=="__main__"):
    app.run(debug=True)
