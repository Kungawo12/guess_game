def start_game():
    import random
    import art
    print(art.logo)
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)
    difficulty= input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        attempts = 5
    elif difficulty == "easy":
        attempts = 10
    else:
        print("Invalid input.")
        attempts = 0

    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == num:
            print(f"You got it! The answer was {num}.")
            break
        elif guess < num:
            print("Too low.")
            attempts -= 1
        elif guess > num:
            print("Too high.")
            attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

    if attempts == 0:
        print(f"You've run out of guesses, you lose. The number was {num}.")