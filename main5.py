from flask import Flask,request ,render_template,redirect

app=Flask("__name__")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login5.html")

    else:#now reuest is post
        name=request.form["name"]
        pwd=request.form["pwd"]
        if( name=="Affan" and pwd=="Affan@21"):
            return render_template("welcome.html",name=name)
        else:
          
            return redirect("/login")
          

if(__name__=="__main__"):
    app.run(debug=True)