import random

easy_words = ["apple","mango","banana","computer","pakistan"]
mediam_words = ["laptop","bottle","python","monkey","planet"]
hard_words = ["elephant","diamond","umbrella","mountains","coding"]

print("Welcome to the password guessing game")
level = input("Choose a difficulty level: easy,medium or hard: ").lower()


if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(mediam_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice.  Diffaulting to easy level")
    secret = random.choice(easy_words)
    
    
attempts = 0
print("Guess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1
    
    if guess == secret:
        print(f"Congratulations! You have guess correctly in {attempts} attempts.")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
    print("Hint:",hint)