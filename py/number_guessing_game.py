import math
import random
lower = int(input("enter the lower bound:"))
upper = int(input("enter the upper bound:"))
x=random.randint(lower,upper)
tries = round(math.log(upper-lower+1,2))
print("you have ",tries," tries")
count = 0
while count < tries:
    count = count + 1
    guess = int(input("guess a number:"))
    if x == guess :
        print("you found the element !")
        print("only took ",count,"to find the element")
        break
    elif x > guess :
        print("too low")
    elif x < guess :
        print("too high")
else:
    print("you failed to find the element" )
    print ("the element is ",x )
