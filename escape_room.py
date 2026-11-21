import random


def ask_choice(prompt, options):
    """Ask until the player enters an allowed answer."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in options:
            return answer
        print("Please enter one of:", ", ".join(options))


def ask_number(prompt, minimum, maximum):
    """Read a whole number inside the specified range."""
    while True:
        try:
            number = int(input(prompt))
            if minimum <= number <= maximum:
                return number
        except ValueError:
            pass
        print(f"Enter a number from {minimum} to {maximum}.")


def room1():
    """Room 1: guess a coin flip to unlock the door."""
    print("\nROOM 1: Coin Flip")
    print("Guess the coin correctly to continue.")
    while True:
        guess = ask_choice("Heads or tails? ", ("heads", "tails"))
        result = random.choice(("heads", "tails"))
        print("The coin landed on", result + ".")
        if guess == result:
            print("Correct! Door unlocked.")
            return
        print("Not quite. Try again!")


def room2():
    """Room 2: win a round of rock-paper-scissors."""
    print("\nROOM 2: Rock Paper Scissors")
    beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    while True:
        user = ask_choice("Rock, paper, or scissors? ", tuple(beats))
        computer = random.choice(tuple(beats))
        print("Computer chose", computer + ".")
        if user == computer:
            print("It's a tie. Try again!")
        elif beats[user] == computer:
            print("You win! Door unlocked.")
            return
        else:
            print("Computer wins this round. Try again!")


def room3():
    """Room 3: guess the secret number between 1 and 10."""
    print("\nROOM 3: Number Guess")
    secret = random.randint(1, 10)
    while True:
        guess = ask_number("Guess a number (1-10): ", 1, 10)
        if guess == secret:
            print("You got it! Door unlocked.")
            return
        print("Too low!" if guess < secret else "Too high!")


def room4():
    """Room 4: answer three trivia questions correctly."""
    print("\nROOM 4: Trivia")
    questions = (
        ("Is 1 + 1 equal to 2? (yes/no): ", "yes"),
        ("Is Toronto the capital of Canada? (yes/no): ", "no"),
        ("Is 50% equal to one half? (yes/no): ", "yes"),
    )
    for prompt, correct in questions:
        while True:
            answer = ask_choice(prompt, ("yes", "no"))
            if answer == correct:
                print("Correct!")
                break
            print("Incorrect. Try again!")
    print("Trivia complete! Door unlocked.")


def room5():
    """Room 5: correctly guess a die roll to escape."""
    print("\nROOM 5: Dice Challenge")
    print("Guess the die roll (1-6) to escape.")
    while True:
        guess = ask_number("Your guess: ", 1, 6)
        result = random.randint(1, 6)
        print("The die rolled", str(result) + ".")
        if guess == result:
            print("You win the final challenge!")
            return
        print("Try again!")


def main():
    """Play all five rooms in order."""
    print("WELCOME TO THE ESCAPE ROOM")
    print("Complete five challenges to escape. Press Ctrl+C to quit.")
    for room in (room1, room2, room3, room4, room5):
        room()
    print("\nCongratulations! You escaped all five rooms!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame closed.")
