from flask import Flask,render_template,request
app=Flask("__name__")

@app.route("/name",methods=["GET","POST"])
def name():
    if request.method=="GET":
        return render_template("f.html")
    else:    
        fname=request.form["fname"]
        lname=request.form["lname"]
        uname=fname+" "+lname
        return render_template("w.html",uname=uname)

if(__name__=="__main__"):
    app.run(debug=True) 