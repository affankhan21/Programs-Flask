from flask import Flask,render_template,request
ret=Flask(__name__)
@ret.route('/hello')
def fy():
    return "hello"
@ret.route("/second")
def second():
    return render_template("second.html")
if(__name__=="__main__"):
    ret.run()#start the server 