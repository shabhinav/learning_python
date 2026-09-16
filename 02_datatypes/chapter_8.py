ingredients = ["water", "milk", "black tea"]

ingredients.append("sugar") # unlike tuple you can add the item on the fly

print(f"Ingredients are: {ingredients}")

ingredients.remove("water")

print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2,"black tea")
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"chai: {chai_ingredients} {last_added}")


chai_ingredients.reverse()
print(f"chai reverse: {chai_ingredients}")


chai_ingredients.sort()
print(f"chai sort: {chai_ingredients}")


sugar_levels = [1,2,3,4,5]

print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Mininmum sugar level: {min(sugar_levels)}")



# operator overloding
base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

full_liquid_mix= base_liquid + extra_flavor
print(f"liquid mix: {full_liquid_mix}")

strong_brew = ["black tea"] * 3
print(f"strong_brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINN",b"CARD")
print(f"raw_spice_data: {raw_spice_data}")
