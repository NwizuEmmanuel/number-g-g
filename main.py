import random
import sys
from datetime import datetime
class NumberGG:
    def __init__(self):
        self.player_level = None
        self.chances_gained = 0
        self.attempts = 0
        self.current_score = 0
        self.guess_number = 50#random.randint(1,100)
        self.player_guess_number = 0
        self.scores = {'easy': 0, 'medium': 0, 'hard': 0}
        self.initial_time = None
        self.finial_time = None
        self.game_intro = """
        Welcome to number guessing game aka number-g-g.
        I am thinking a number between 1 and 100

        Select your levels:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)
        """

    def hint(self):
        choice = ''
        start_steps = self.guess_number - 3
        end_steps = self.guess_number + 3
        if self.chances_gained == 3:
            choice = input("Do you want a hint? y/n")
        elif self.chances_gained == 5 and self.attempts == 3:
            choice = input("Do you want a hint? y/n")
        elif self.chances_gained == 10 and self.attempts == 5:
            choice = input("Do you want a hint? y/n")

        if choice.lower() == 'y':
            print(f"The number is between {start_steps} - {end_steps}")
        elif choice.lower() == 'n':
            print("Ok. Good luck.")

    def get_timer(self):
        format = "%H:%M:%S"
        t1 = datetime.strptime(self.initial_time, format)
        t2 = datetime.strptime(self.finial_time, format)
        difference = t2 - t1
        seconds = difference.total_seconds()
        return f"Game play time: {seconds}s"

    def calculate_score(self):
        level_chances = self.chances_gained
        self.current_score = (level_chances - self.attempts)
        if self.player_guess_number == self.guess_number and self.current_score == 0:
            self.current_score += 1
        else:
            self.current_score += 1

    def save_score(self):
        levels = {1: 'easy', 2: 'medium', 3: 'hard'}
        previous_score = self.scores[levels[self.player_level]]
        if self.current_score > previous_score:
            self.scores[levels[self.player_level]] = self.current_score

    def highest_score(self):
        levels = {1: 'easy', 2: 'medium', 3: 'hard'}
        previous_score = self.scores[levels[self.player_level]]
        if previous_score > self.current_score:
            print(f"Highest score: {previous_score}")
        else:
            print(f"Highest score: {self.current_score}")

    def set_chances(self, player_level):
        game_chances = [10,5,3]
        if player_level == 1:
            return 10
        elif player_level == 2:
            return 5
        elif player_level == 3:
            return 3
        else:
            return 0

    def level_info(self):
        result = {
            10: "Great! you have selected Easy level.",
            5: "Great! you have selected Medium level.",
            3: "Great! you have selected Hard level."
        }
        return result

    def choose_level(self):
        while True:
            try:
                self.player_level = int(input("Choose your level? "))
                self.chances_gained = self.set_chances(self.player_level)
                print(self.level_info()[self.chances_gained])
                print("Let's start the game.")
                return False
            except (ValueError, KeyError):
                print("Level is not available.")

    def guessing(self):
        while True:
            try:
                self.player_guess_number = int(input("Enter your guess: "))
                self.attempts += 1
                print(f"Attempts=> {self.attempts}")
                if self.guess_number > self.player_guess_number:
                    print(f"No! The number is greater than {self.player_guess_number}")
                if self.guess_number < self.player_guess_number:
                    print(f"No! The number is less than {self.player_guess_number}")
                self.hint()
                if self.guess_number == self.player_guess_number:
                    print(f"You win! You guessed the number in the {self.attempts} attempt.")
                    self.calculate_score()
                    self.save_score()
                    print(f"Current score: {self.current_score}")
                    self.highest_score()
                    self.finial_time = datetime.now().strftime("%H:%M:%S")
                    return False
                if self.attempts == self.chances_gained:
                    print(f"Game over. You lose. The number is {self.guess_number}")
                    self.calculate_score()
                    self.save_score()
                    print(f"Current score: {self.current_score}")
                    self.highest_score()
                    self.finial_time = datetime.now().strftime("%H:%M:%S")
                    return False
            except ValueError:
                print("Not a number.")

    def replay(self):
        self.attempts = 0
        while True:
            choice = input("Do you want play again? yes(y) or no(n) ")
            if choice.lower() == 'n':
                sys.exit(0)
            elif choice.lower() == 'y':
                return False
            else:
                print("I don't know what u said. So lets end the game.")
                print("If u want to play again, replay the game.")
                sys.exit(0)


    def start_game_loop(self):
        while True:
            print(self.game_intro)
            self.choose_level()
            self.initial_time = datetime.now().strftime("%H:%M:%S")
            self.guessing()
            print(self.get_timer())
            self.replay()
            print("next")

def main():
    game = NumberGG()
    game.start_game_loop()

if __name__ == "__main__":
    main()

