class PlayTypeByTurn:

    def __init__(self, type, turn):
        self.type = type
        self.turn = turn

    def score_func(self, state):
        score = 0.1
        for card in state.hand:
            if self.type in card.types:
                score += 50
        
        if state.turn_counter > self.turn:
            return 0
        elif self.goal_func(state):
            return 10000
        else:
            return score + state.get_availabale_mana().get_amount()
        
    def goal_func(self, state):
        for card in state.battlefield:
            if self.type in card.types:
                return True
        return False