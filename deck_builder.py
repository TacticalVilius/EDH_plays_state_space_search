import requests
from mana import Mana
from card import Card

class DeckBuilder:

    def __init__(self, file_name):
        self.file_name = file_name
        
    def get_deck(self):
        deck = []
        card_names = self.get_card_names()
        for card_name in card_names:
            print('generating ' + str(card_names[card_name]) + 'x ' + card_name)
            deck += self.generate_cards(self.retrieve_card_info(card_name), card_names[card_name])
        return deck
        
    def get_card_names(self):
        card_names = {}
        with open(self.file_name, 'r') as file:
            for line in file:
                if len(line.strip()) == 0:
                    continue
                parts = line.strip().split('\t')
                number = int(parts[0])
                name = parts[1]
                card_names[name] = number
        return card_names
        
    def retrieve_card_info(self, card_name):
        return requests.get('http://scry.me.uk/api?name=' + card_name).json()
        
    def generate_cards(self, card_info, number):
        if ('error' in card_info):
            print('ERROR: ' + card_info['error'])
            return []
        cards = []
        name = card_info['name']
        types = [type for sublist in [types.strip().split(' ') for types in card_info['types'].split('\u2014')] for type in sublist]
        mana_cost = Mana.of_str_rep(card_info['mana_cost']) if 'mana_cost' in card_info else Mana()
        taps_for_mana = Mana.of_green(1)
        for i in range(number):
            cards.append(Card(name, types, mana_cost, taps_for_mana))
        return cards