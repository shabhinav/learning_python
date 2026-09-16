essential_spices = {"Cardamom","ginger","cinnamon"}
optional_spice = {"clove","ginger","black pepper"}

all_spices = essential_spices | optional_spice
common_spices = essential_spices & optional_spice

print(f"all spices: {all_spices}")
print(f"common spices: {common_spices}")


only_in_essential = essential_spices - optional_spice
print(f"only_in_essential: {only_in_essential}")

#membership test
print(f"Is 'cloves' in essential spices? {"clove" in optional_spice}")

