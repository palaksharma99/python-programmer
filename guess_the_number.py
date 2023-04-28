import random as r
c = 'Guess The Number Game'
b = c.center(50,'#')
print(b)
a = int(input("enter the number of turns : "))
low = int(input(" enter lower limit : "))
up = int(input(" enter upper limit : "))
out = r.randint(low,up)
for i in range(a):
        n = int(input('choose a number between your choosen range : '))
        if out==n:
            print("you guessed it right!")
            break
        elif (out> n):
            print("too small")
        elif (n>up or n<low):
            print("please enter a number within the range")
        else:
            print("too large")
