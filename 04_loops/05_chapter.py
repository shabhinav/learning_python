names = ["hitesh","Meera","sam","ali"]
bills = [50,55,70,100]

for name, amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")