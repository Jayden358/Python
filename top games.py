#Jayden Williams
#10/19
import random

high_scores=[1000,950,850,700,675,550,443,414,395,380]
prices=[9.99,10.25,19.99,100.0]
#dog_breeds["Poodle","Collie","Terrier","Beagle"]
logical_results =[True,True,False,True]
my_collection=[1000,3.14159,"Carrots",False]

top_games=["Red Dead Redemption 2","Grand Theft Auto 5","The Last Of Us","Detroit Become Human",
"Resident Evil 2 REmake","Call Of Duty Modern Warfare (2019)","God Of War (2018)","Judgement",
"Yakuza 0","Final Fantasy 15","Forza Horizon 4","Rainbow 6 Siege","CSGO","TF2","BattleField 4","Hitman(2016",
"Final Fantasy 14","Starfox 2","Mario Maker 2","Fortnite"]

print(type(top_games))

print(len(top_games))
##print(top_games)
##print(top_games[0:5])
##for i in top_games:
##    print(i)
##for i in range(0,len(top_games)):
##    print(top_games[i])
num = random.randint(0,len(top_games)-1)
print(top_games[num])               
if len(top_games) <20:
    print("fail")
for i in top_games:
    if i == "Red Dead Redemption 2":
        print("you are a true gamer")
    else:
        print("not a true gamer")
top_games[19] = "Roblox"        
print(top_games)

    
