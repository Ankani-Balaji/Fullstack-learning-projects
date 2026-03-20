import random

def play_game(limit_range):
    attempts = 10
    secret_number = random.randint(1,limit_range)

    for i in range(attempts):
        print("Attempts left:", attempts-i)

        try:
            guess = int(input(f"Enter your Guess (1 - {limit_range}): "))
        except ValueError:
            print("Invalid input...! Enter a number.")
            continue

        if guess < 1 or guess > limit_range:
            print(f"Enter a number between 1 and {limit_range}")
            continue
        
        if guess > secret_number:
            print("Too High.., Try again!") 
        elif guess < secret_number:
            print("Too Low.., Try again!")
        else:
            print("🎉 Correct!")
            score = (attempts - i) * 10
            print("Your Score is: ",score)
            return True
    else:
        print("Game Over..! The number was:", secret_number)
        return False

def main():
    print("\n🎯 Welcome to Number Guessing Game!")
    print("===================================")
    while True:
        print("--------Game Mode level---------")
        print("1. Easy Mode")
        print("2. Medium Mode")
        print("3. Hard Mode")

        choice = input("Enter Your Choice...!")

        if choice == "1":
            play_game(50)
        elif choice == "2":
            play_game(100)
        elif choice == "3":
            play_game(500)
        else:
            print("Enter Valid Choice.......!")
            continue

        replay = input("Do you want to play again? (y/n): ")
        if replay.lower() != "y":
            print("Exiting the Game...")
            break 
main()