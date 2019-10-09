#Jayden Williams
#9/19
#coin flip
import random

def coin_flip():
    coin = random.randint(1,2)
    if coin is 1:
        coin = coin.replace("1","heads")
        print(coin)
    else:
        coin = coin.replace("2","tails")   
        print(coin)

coin_flip()    
