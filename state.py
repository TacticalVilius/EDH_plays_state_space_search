from copy import deepcopy

from card import Card
from mana import Mana

class State:

    def __init__(self, library, hand, battlefield, prev_action, parent):
        self._library = deepcopy(library)
        self._hand = deepcopy(hand)
        self._battlefield = deepcopy(battlefield)
        self._prev_action = prev_action
        
        self._floating_mana = Mana()
        self._turn_counter = 1
        self._parent = parent
        
    def tap_all_for_mana(self):
        new_state = State(self._library, self._hand, self._battlefield, 'tap all for mana', self)
        for card in new_state._battlefield:
            if not card.is_tapped:
                new_state._add_floating_mana(card.tap_for_mana())
        if self != new_state:
            return new_state
        else:
            return None
            
    def get_availabale_mana(self):
        mana = Mana()
        for card in self._battlefield:
            if not card.is_tapped:
                mana += card.taps_for_mana
        return mana + self._floating_mana
        
    def play_card(self, card_name):
        new_state = State(self._library, self._hand, self._battlefield, 'play ' + card_name, self)
        card = new_state._get_card_in_hand(card_name)
        
        new_state._hand.remove(card)
        new_state._battlefield.append(card)
        new_state._remove_floating_mana(card.mana_cost)
        return new_state
        
    def get_playable_cards(self):
        playable_cards = []
        for card in self.hand:
            if self._floating_mana.fulfils_cost(card.mana_cost.mana):
                playable_cards.append(deepcopy(card))
        return playable_cards
        
    def new_turn(self):
        if len(self._library == 0):
            return None
            
        new_state = State(self._library, self._hand, self._battlefield, 'new turn', self)
        
        new_state._untap_all()
        new_state._floating_mana = Mana()
        new_state._draw_card()
        new_state._turn_counter += 1
        
        return new_state

    def describe(self):
        return "Turn number: " + str(self.turn_counter) + " library size: " + str(len(self.library)) + " hand size: " + str(len(self.hand)) + " battlefield size: " + str(len(self.battlefield)) + " available mana: " + str(self.get_availabale_mana().get_amount()) + " " + self.prev_action
        
    def _get_card_in_hand(self, card_name):
        for card in self._hand:
            if card.name == card_name:
                return card
        return None
        
    def _add_floating_mana(self, mana):
        self._floating_mana += mana
        
    def _remove_floating_mana(self, mana):
        self._floating_mana -= mana

    def _untap_all(self):
        for card in self._battlefield:
            card.untap()
        
    def _draw_card(self):
        self.hand += self.library[-1:]
        self.library = self.library[:-1]
    
    # TODO: eq, ne, hash