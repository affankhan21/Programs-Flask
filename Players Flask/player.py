import os
class Player:
    def __init__(self,pname,age,role,runs=0,matches=0,wickets=0):
        if(not os.path.exists("player.txt")):
            self.pid = 101
        else:
            if os.path.getsize("player.txt") > 0:
                with open("player.txt","r") as fp:                
                    for player in fp:
                        pass
                self.pid = int( player.split(",")[0])+1
            else:
                self.pid = 101
                
        self.pname = pname
        self.age = age
        self.role = role
        self.runs = runs
        self.matches = matches
        self.wickets = wickets

    def __str__(self):
        data = str(self.pid)
        data+= "," + self.pname
        data+="," + str(self.age)
        data+="," + self.role
        data+="," + str(self.runs)
        data+="," + str(self.matches)
        data+="," + str(self.wickets)
        return data
        
        
