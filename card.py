class Card:

    def __init__(self, name, types, mana_cost, taps_for_mana):
        self.name = name
        self.types = types
        self.mana_cost = mana_cost
        self.taps_for_mana = taps_for_mana
        
        self.is_tapped = False
        
    def tap_for_mana(self):
        self.is_tapped = true
        return taps_for_mana

    def untap(self):
        self.is_tapped = False