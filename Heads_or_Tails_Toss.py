import random
import time
toss=random.randint(0,1)

choice=input("What would you choose? Heads or Tails?\n")
print("Doing a Toss....!")
time.sleep(5)
if choice=="Heads":
    if toss==0:
        print("Its Head!")
    else:
        print("Sorry, Its Tails!")
elif choice=="Tails":
    if toss==1:
        print("Its Tails!")
    else:
        print("Sorry! Its Heads!")
