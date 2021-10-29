def guess(x):
    rand_num = random.randint(1,x)
    guess = 0
    while guess != rand_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < rand_num:
            print("Wrong Answer, your guess is too low!Try it again")
        elif guess > rand_num:
            print("Wrong Answer, your guess is too high!Try it again")
    print(f"Good! You Win. You have guessed the number: {rand_num}")

guess(10)