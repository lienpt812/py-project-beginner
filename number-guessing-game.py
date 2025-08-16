import random, math
def guess(low,up) -> int:
    while True:
        num_guess = int(input("Enter the guess number: "))
        if num_guess not in range(low,up+1):
            print("Invalid number!")
            continue
        else:
            return num_guess
        
try:
    print("Welcome to the Number Guessing Game!!!".center(50,"-"))
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    num_correct = random.randint(lower,upper+1)
    total_chances = int(math.ceil(math.log2(upper-lower+1)))
    print("You've only", total_chances, "chances!")
    cnt = 0
    while cnt < total_chances:
        num_guess = guess(lower,upper)
        cnt +=1
        if num_guess > num_correct:
            print("Try Again! Your number is too high!")
        elif num_guess < num_correct:
            print("Try Again! Your number is too low!")
        else:
            print(f"Congrats!!! The correct number is {num_correct}. You did it in {cnt} try")
            break
    else: print(f"Oops, out of chances.. The correct number is {num_correct}. Better luck next time!")
except ValueError as e:
    print(e)