import random
'''
1 = rock
-1 = paper
0 = scissors
'''
print("Rule 1:select p for paper")
print("Rule 2:select s for scissors")
print("Rule 3:select r for rock")
computer = random.choice([1,-1,0])
youstr = input("Enter your choice: ")
youdict = {"r":1,"p":-1,"s":0}
you = youdict[youstr]
reversedict = {1:"Rock",-1:"Paper",0:"Scissor"}

print(f"you choose: {reversedict[you]}\ncomputer choose: {reversedict[computer]}")


if(computer == you):
        print("This is draw")
else:

    if(computer == 1 and you == 0):
        print("You lose ")

    elif(computer == 1 and you == -1):
        print("You win!!! ")

    elif(computer == -1 and you == 0):
        print("You win!!! ")

    elif(computer == -1 and you == 1):
        print("You lose ")

    elif(computer == 0 and you == -1):
        print("You lose ")

    elif(computer == 0 and you == 1):
        print("You win!!! ")
    else:
        print("something went wrong")

    