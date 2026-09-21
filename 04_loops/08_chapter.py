staff = [("amit",16),("zara",13),("Raj",21)]

for name, age in staff:
    if age >=18:
        print(f"{name} is eligible for working staff")
        break
    else:
        print("No one is eligible")
    