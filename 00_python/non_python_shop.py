class Chai:
    def __init__(self,sweetness, milk_lvl):
        self.sweetness = sweetness
        self.milk_lvl = milk_lvl
    
    def sip(self):
        print("Sipping Chai")

    def add_ssugar(self, amount):
        print("Added the sugar")

my_chai = Chai(sweetness= 3, milk_lvl= 3)

my_chai.add_ssugar