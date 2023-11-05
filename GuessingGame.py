import random

def guess_the_number():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if user_guess < target_number:
            print("Too low. Try again.")
        elif user_guess > target_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
            break

if __name__ == "__main":
  guess_the_number()
