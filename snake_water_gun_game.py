import random
'''
1 for snake
0 for gun
-1 for water
'''


computer = random.choice([1,0,-1])
youstr = input("Enter your choice: ")
youdict = {"s":1,"g":0,"w":-1}
reverseDict = {1:"snake",0:"gun",-1:"water"}
you = youdict[youstr]

print(f"You choose {reverseDict[you]}\ncomputer choose {reverseDict[computer]}")

if(computer==you):
    print("It's Draw")
else:
    if(computer==-1 and you==1):
        print("You win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You win!")
    elif(computer==0 and you==-1):
        print("You win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    else:
        print("Something went wrong")
