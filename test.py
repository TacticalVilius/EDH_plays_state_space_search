from copy import copy

class Test:

    def __init__(self, value):
        self.value = value

    def deccc(self, value):
        return value - 1
        
    def print_value(self):
        print(self.deccc(self.value))
        
def main():
    t1 = Test(3)
    l = [t1] * 2
    print(l)
    print([l[0].value, l[1].value])
    l[0].value = 17
    print([l[0].value, l[1].value])
    
if __name__ == "__main__":
    main()