from flask import Flask,request,render_template,redirect

app=Flask("__name__")


@app.route("/firstqs",methods=["GET","POST"])
def queryStringDemo1():
    if request.method == "GET":
        return render_template("first_qs.html")
    else:
        fname = request.form["fname"]
        lname = request.form["lname"]
        age = int(request.form["age"])

        if age < 18 :
            return "You are not eligible to vote"
        else:
            urls = "/acceptVote?fname="+fname+"&lname="+lname
            return redirect(urls)



@app.route("/acceptVote",methods=["GET","POST"])
def acceptVote():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    if request.method == "GET":        
        return render_template("vote.html",fname=fname,lname=lname)
    else:
        choice = int(request.form["choice"])
        subject = ""
        if choice == 1:
            subject = "Java"
        elif choice == 2:
            subject = "Python"
        elif choice == 3:
            subject = "Software Testing" 
        return render_template("votingResult.html",fname=fname,lname=lname,subject=subject)
if(__name__=="__main__"):
    app.run(debug=True)