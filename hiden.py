from flask import Flask,request,render_template

app=Flask("__name__")
@app.route("/hiddenDemo",methods=["GET","POST"])
def hiddenDemo():
    if request.method == "GET":
        return render_template("hidden.html")
    else:
        fname = request.form["fname"]
        lname = request.form["lname"]
        uname = fname+" "+lname
        return render_template("hidden.html",uname=uname)
@app.route("/clickCount",methods=["GET","POST"])
def clickCount():
    if request.method == "GET":
        clicks_count = 0
        return render_template("countclick.html",clicks_count = clicks_count)
    else:
        clicks_count = int(request.form["clicks_count"])
        clicks_count+=1
        return render_template("countclick.html",clicks_count = clicks_count)


if(__name__=="__main__"):
    app.run(debug=True)