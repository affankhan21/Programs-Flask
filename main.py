from flask import Flask
app=Flask(__name__)
@app.route("/welcome")
def method1():
    return "Welcome to my first flask application!!"
@app.route("/curve")  
def method2():
    return  " flask has easy learning"
@app.route("/enjoy")    
def method3():
    return "you will enjoy!!!!!"        

if(__name__=="__main__"):
    app.run(debug=True)