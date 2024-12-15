import random

class NumberGG:
    def __init__(self):
        self.gained_chances = 0
        self.current_chances = 0
        self.the_number = random.randint(1,100)
        self.player_guess = 0
    def intro(self):
        result = """
        Welcome to number guessing game aka number-g-g.
        I am thinking a number between 1 and 100

        Select your levels:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances)
        """
        return result

    def get_chances(self, level):
        chances = [10,5,3]
        self.gained_chances = chances[level-1]


    def check_number(self,number):
        if self.current_chances == self.gained_chances:
            print(f"Game over. The number is {self.the_number}({self.current_chances} attempts).")
        elif number > self.the_number:
            print(f"{number} is greater than the number({self.current_chances} attempts).")
        elif number < self.the_number:
            print(f"{number} is less than the number({self.current_chances} attempts).")
        elif number == self.the_number:
            print(f"Congratutions. The number is {self.the_number}({self.current_chances} attempts).")


    def start_game(self):
        print(self.intro())
        while True:
            user_level = int(input("Enter level here: "))
            self.get_chances(user_level)
            if user_level in [1,2,3]:
                break
            else:
                print('invalid level.')

        while True:
            try:
                if self.gained_chances == self.current_chances or self.player_guess == self.the_number:
                    want_replay = input("Do you want to play again? [y/n]")
                    break
                else:
                    self.current_chances += 1 
                self.player_guess = int(input("What's the number? "))
                self.check_number(self.player_guess)
            except Exception:
                print("Not a number.")



def main():
    game = NumberGG()
    game.start_game()

if __name__ == "__main__":
    main()

