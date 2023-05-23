import random

class Dilemma:
    def __init__(self):
        self.matrix = {(0, 0): (1, 1),
                (0, 1): (0, 5),
                (1, 0): (5, 0),
                (1, 1): (3, 3)}

    # 0 = Defect; 1 = Cooperate
    def action(self):
        return random.randint(0, 1)

    def payoff(self, a, b):
            return self.matrix[(a, b)]

    def game(self):
        rounds = 33
        
        for n in range(rounds):
            a = self.action()
            b = self.action()
            result = self.payoff(a, b)
            print(f'({n}) A: {a}, B:{b} = {result}')

prisoner = Dilemma()
prisoner.game()