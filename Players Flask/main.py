from flask import Flask,render_template,redirect,request,session
from player import Player

app = Flask(__name__)
app.secret_key="1233"

@app.route("/addPlayer",methods=["GET","POST"])
def addPlayer():
    if request.method=="GET":
        return render_template("addRecord.html")
    else:
        pname = request.form["pname"]
        age = request.form["age"]
        role = request.form["role"]
        runs = request.form["runs"]
        wickets = request.form["wickets"]
        matches = request.form["matches"]
        p1 = Player(pname,age,role,runs,matches,wickets)
        with open("player.txt","a") as fp:
            fp.write(str(p1)+"\n")
        return redirect("/showAllPlayers")
    
@app.route("/showAllPlayers")
def showAllPlayers():
    players = []
    with open("player.txt","r") as fp:
            for player in fp:
                player = player.strip().split(",")
                players.append(player)
    return render_template("showAllPlayers.html",players = players)

@app.route("/deleteRecord/<id>",methods=["GET","POST"])
def deleteRecord(id):
    players = []
    with open("player.txt","r") as fp:
            for player in fp:
                player = player.strip().split(",")
                if int(id) != int(player[0]):
                    players.append(player)
            print(players)
    with open("player.txt","w") as fp:
        for player in players:
           player = ",".join(player)
           fp.write(player+"\n")
        
    return redirect("/showAllPlayers")
                

@app.route("/editRecord/<id>",methods=["GET","POST"])
def editRecord(id):
    if(request.method=="GET"):        
        with open("player.txt","r") as fp:  
            for player in fp:
                player = player.strip().split(",")
                if int(id) == int(player[0]):
                    break
        return render_template("editPlayer.html",player=player)    
    else:
        allPlayers = []
        with open("player.txt","r") as fp:  
            for player in fp:
                player = player.strip().split(",")
                if int(id) == int(player[0]):
                    pname = request.form["pname"]
                    age = request.form["age"]
                    role = request.form["role"]
                    runs = request.form["runs"]
                    wickets = request.form["wickets"]
                    matches = request.form["matches"]
                    p1 = Player(pname,age,role,runs,matches,wickets)
                    player = str(p1)+"\n"
                else:
                    player= ",".join(player)+"\n"
                allPlayers.append(player)
        with open("player.txt","w") as fp:
            for player in allPlayers:
                fp.write(player)
        return redirect("/showAllPlayers")

                



if __name__ == "__main__":
    app.run(debug=True)