import random
from enum import Enum

DEFAULT_ROUNDS = 33

class Action(Enum):
    COOPERATE = 0
    DEFECT = 1

class Dilemma:
    """Modelling the Prisoner's Dilemma game."""
    def __init__(self):
        self.matrix = {(Action.COOPERATE, Action.COOPERATE): (3, 3),
                (Action.COOPERATE, Action.DEFECT): (0, 5),
                (Action.DEFECT, Action.COOPERATE): (5, 0),
                (Action.DEFECT, Action.DEFECT): (1, 1)}
        self.strategy_a = self.random_action
        self.strategy_b = self.random_action

    def random_action(self, _, __, ___) -> Action:
        return random.choice(list(Action))
    
    def play_tit_for_tat(self, opponent_history, _, __) -> Action:
        if not opponent_history:
            return Action.COOPERATE
        return opponent_history[-1]
    
    def hold_grudge(self, opponent_history, _, __) -> Action:
        if Action.DEFECT in opponent_history:
            return Action.DEFECT
        return Action.COOPERATE
    
    def play_pavlov(self, _, payoff_history, player_index) -> Action:
        if len(payoff_history) < 2:
            return Action.DEFECT
        else:
            return Action.DEFECT if payoff_history[-1][player_index] < payoff_history[-2][player_index] else Action.COOPERATE

    def get_payoff(self, a, b):
        return self.matrix[(a, b)]
        
    def analyse(self, data):
        return data.count(Action.COOPERATE), data.count(Action.DEFECT)

    def play_game(self, rounds=DEFAULT_ROUNDS):
        history_a = []
        history_b = []
        payoff_history = []
        for n in range(rounds):
            a = self.strategy_a(history_b, payoff_history, 0)
            b = self.strategy_b(history_a, payoff_history, 1)
            history_a.append(a)
            history_b.append(b)
            payoff_history.append(self.get_payoff(a, b))
            print(f'({n}) A: {a}, B:{b} = {payoff_history[-1]}')
            
        actions_a = self.analyse(history_a)
        actions_b = self.analyse(history_b)
        payout_a, payout_b = map(sum, zip(*payoff_history))
        print(f'(COOPERATE, DEFECT) ~ Payout\nA: {(actions_a)} ~ {payout_a}\nB: {(actions_b)} ~ {payout_b}')

prisoner = Dilemma()
prisoner.strategy_a = prisoner.random_action
prisoner.strategy_b = prisoner.play_pavlov
prisoner.play_game()