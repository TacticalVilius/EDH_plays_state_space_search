from color import Color

class Mana:

    def __init__(self):
        self.mana = {
            Color.white : 0,
            Color.blue : 0,
            Color.black : 0,
            Color.red : 0,
            Color.green : 0,
            Color.colorless : 0,
            'generic' : 0
        }
    
    @staticmethod
    def of(white, blue, black, red, green, colorless, generic):
        m = Mana()
        m.mana = {
            Color.white : white,
            Color.blue : blue,
            Color.black : black,
            Color.red : red,
            Color.green : green,
            Color.colorless : colorless,
            'generic' : generic
        }
        return m
    
    @staticmethod
    def of_white(white):
        return Mana.of(white, 0, 0, 0, 0, 0, 0)
        
    @staticmethod
    def of_blue(blue):
        return Mana.of(0, blue, 0, 0, 0, 0, 0)
    
    @staticmethod
    def of_black(black):
        return Mana.of(0, 0, black, 0, 0, 0, 0)
        
    @staticmethod
    def of_red(red):
        return Mana.of(0, 0, 0, red, 0, 0, 0)
        
    @staticmethod
    def of_green(green):
        return Mana.of(0, 0, 0, 0, green, 0, 0)
        
    @staticmethod
    def of_colorless(colorless):
        return Mana.of(0, 0, 0, 0, 0, colorless, 0)
        
    @staticmethod
    def of_generic(generic):
        return Mana.of(0, 0, 0, 0, 0, 0, generic)
    
    @staticmethod
    def of_str_rep(str_rep):
        m = Mana()
        costs = [cost for temp_list in [str.split('{') for str in str_rep.split('}')] for cost in temp_list if len(cost) > 0]
        for cost in costs:
            if cost.isdigit():
                m += Mana.of_generic(int(cost))
            elif cost == 'W':
                m += Mana.of_white(1)
            elif cost == 'U':
                m += Mana.of_blue(1)
            elif cost == 'B':
                m += Mana.of_black(1)
            elif cost == 'R':
                m += Mana.of_red(1)
            elif cost == 'G':
                m += Mana.of_green(1)
            elif cost == 'C':
                m += Mana.of_colorless(1)
        return m
    
    def __add__(self, other):
        return Mana.of(self.mana[Color.white] + other.mana[Color.white],
            self.mana[Color.blue] + other.mana[Color.blue],
            self.mana[Color.black] + other.mana[Color.black],
            self.mana[Color.red] + other.mana[Color.red],
            self.mana[Color.green] + other.mana[Color.green],
            self.mana[Color.colorless] + other.mana[Color.colorless],
            self.mana['generic'] + other.mana['generic'])
            
    def __sub__(self, other):
        return Mana.of(self.mana[Color.white] - other.mana[Color.white],
            self.mana[Color.blue] - other.mana[Color.blue],
            self.mana[Color.black] - other.mana[Color.black],
            self.mana[Color.red] - other.mana[Color.red],
            self.mana[Color.green] - other.mana[Color.green],
            self.mana[Color.colorless] - other.mana[Color.colorless],
            self.mana['generic'] - other.mana['generic'])
        
    def fulfils_cost(self, cost):
        for color in Color:
            if cost[color] > self.mana[color]:
                return False
        return sum(cost.values()) <= sum(self.mana.values())
    
    def get_amount(self):
        return sum(self.mana.values())