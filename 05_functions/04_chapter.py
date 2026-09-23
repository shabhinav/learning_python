chai = "giner chai"

def prepare_chai(order):
    print(f"preparing ",order)


prepare_chai(chai)

chai = [1,2,3]

def edit_chai(cup):
    cup[1] = 42


edit_chai(chai)


def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("Darjeeling","Yes","Low")
make_chai(tea="green",sugar="Medium",milk="Yes")

def special_chai(*ingredients,**extras):
    print("Ingredients",ingredients)
    print("Extras",extras)

    special_chai("Cinnamon","Cardamom",Sweetner="Honey",foam="yes")

    def chai_order(order=[]):
        order.append("Masala")

        chai_order()
        chai_order()
 