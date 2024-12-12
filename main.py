import random

class NubmberGG:
    def __init__(self):
        self.intro = """
Welcome to number-g-g aka number guessing game.
I am thinking a number between 1 and 100

Please select a difficulty level.
1. Easy -> 10 chances
2. Medium -> 5 chances
3. Hard -> 3 chances
"""
        print(self.intro)
        self.current_chance = 0
        self.number_to_guess = random.randint(1,100)


    def check_player_number(self, number):
        if self.number_to_guess > number:
            print(f"The number is greater than {number}")
        elif self.number_to_guess < number:
            print(f"The number is less than {number}")
        elif self.number_to_guess == number:
            print(f"Congratulations you guessed the number in {self.current_chance} attempts.")


    def start_game(self):
        """Function: for starting game"""

        # checks user input is a correct level
        while True:
            selected_chances = int(input("Enter here:"))
            if selected_chances in [3,5,10]:
                break
        
        # run the game loop
        while True:
            self.current_chance += 1
            player_number = int(input("Enter your guess: "))
            self.check_player_number(player_number)
            if self.current_chance == selected_chances:
                print(f"Game over. The number is {self.number_to_guess}.")
                break
            elif player_number == self.number_to_guess:
                break

def main():
    game = NubmberGG()
    game.start_game()


if __name__ == "__main__":
    main()