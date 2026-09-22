def get_input():
    print("Getting user input")


def valudate_input():
    print("validate  the user")


def save_to_db():
    print("saving to DB")

def calling_functions():
    save_to_db()
    valudate_input()
    get_input()


def calculate_bills(cups,price_per_cups):
    return cups * price_per_cups

my_bill = calculate_bills(3,15)
print(my_bill)

def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders= [100,150,200]


for price in orders:
    final_amount  = add_vat(price,10)
    print(f"final wamount {final_amount}")
