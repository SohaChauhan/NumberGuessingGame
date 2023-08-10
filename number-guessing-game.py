import random
import math

lower=int(input("Enter the lower bound of the range:"))
upper=int(input("Enter the upper bound of the range:"))

number=random.randint(lower,upper)

number_of_tries=int(math.log(upper-lower+1,2));
flag=0
for i in reversed(range(number_of_tries)):
    n=int(input("Guess an integer:"))
    if n==number:
        print("Your guessed correctly in",number_of_tries-i,"tries!!")
        flag=1
        break;
    else:
        if n>number:
            print("You guessed too high!")
        else:
            print("You guessed too low!")
if flag==0:
    print("You are out of tries!")
    print("The number was",number)
    print("Better luck next time!!")
    