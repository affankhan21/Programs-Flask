from flask import Flask,request,make_response,redirect,render_template
app=Flask("__name__")
@app.route("/cc",methods=["GET","POST"])
def clickc():
    
    if request.method == "GET":
        ccount = 0
        return render_template("cc.html",ccount = ccount)
    else:
        ccount = int(request.form["ccount"])
        ccount+=1
        return render_template("cc.html",ccount = ccount)


if(__name__=="__main__"):
    app.run(debug=True)