from player import Player

p1 = Player("Raghav",22,"Batsman",100,10,4)

fp = open("player.txt","a")
fp.write(str(p1)+"\n")
fp.close()