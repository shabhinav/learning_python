flavors = ["ginger","Out of stock","Lemon","Discountinued","Tulsi"]


for flavor in flavors:
    if flavor == "Out of stock":
        continue
    if flavor == "Discountinued":
        print("Discountined item found")
        break

print("Outside of loop")