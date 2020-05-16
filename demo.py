import random
def throwDice():
    outcome=[random.randint(1,6),random.randint(1,6)]
    return outcome
noOfPlayers=int(input("Enter no of players:"))
players={}
win=False
winner=""
for i in range(noOfPlayers):
    players['Player_'+str(i+1)]=input("Enter player "+str(i+1)+" name:")
while(True): #Game Infinite
    for player in players:
        print(players[player],"turn:")
        input("Press enter to throw dice!")
        outcome=throwDice()
        print(outcome)
        if(outcome[0]==outcome[1]):
            print("Game Over!")
            print("Player",players[player],"wins")
            win=True
            break    
    if(win):
        break
