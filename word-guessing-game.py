import random

print("Welcome to Word Guessing Game!!!".center(50, "-"))
name = input("Input your name: ")
print(f"Good luck, {name}!")
words = ['python', 'love', 'story', 'sick', 'sunny',
         'player', 'apple', 'cake', 'socola', 'quality',
         'tuple','traceback', 'argument', 'project', 'module']
word = random.choice(words)
total_choices = 10
print(f"You've only {total_choices} choices!")
cnt = 0
guesses = ''
while cnt < total_choices:
    cnt+=1
    failed = 0
    char = input("Guess a character: ")
    if char not in word:
        print(f"Wrong! '{char}' is not in word!. Try Again!!")
        continue
    else:
        guesses += char
        for c in word:
            if c in guesses:
                print(c, end="")
            else:
                print("-", end="")
                failed += 1
    print()
    if failed == 0:
        print(f"You win!! The word is '{word}'")
        break
else:
    print(f"You lose! The word is '{word}'")