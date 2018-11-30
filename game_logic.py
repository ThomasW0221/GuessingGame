import random


class Game:

    def __init__(self):
        self.number = random.randint(1, 11)
        self.num_guesses = 0
        self.guessed = False
        self.guess_status = ""

    def guess(self, guess):
        if guess < self.number:
            self.num_guesses += 1
            self.guess_status = "Your guess is too low"

        elif guess > self.number:
            self.num_guesses += 1
            self.guess_status = "Your guess is too high"

        else:
            self.num_guesses += 1
            self.guessed = True
            self.guess_status = "Your guess is correct"

    def check_win(self):
        if self.guessed is True and self.num_guesses <= 3:
            return "win"
        else:
            if self.guessed is False and self.num_guesses < 3:
                return "play"
            else:
                return "lose"

    def reset(self):
        self.number = random.randint(1, 11)
        self.num_guesses = 0
        self.guessed = False
        self.guess_status = ""
