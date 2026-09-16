masala_spices = ("cardamom", "clove", "cinnamom", "ginger")

(spice1, spice2, spaice3, spaice4) = masala_spices


print(f"Main masala spaices: {spice1}, {spice2}, {spaice3}" )

ginger_ratio, cardamon_ratio = 2,1 # short hand property for the tuple

print(f"Ratio is G {ginger_ratio} and {cardamon_ratio}")

ginger_ratio, cardamon_ratio = cardamon_ratio,ginger_ratio

print(f"Ratio is G {ginger_ratio} and {cardamon_ratio}")

# membership testing

print(f"Is ginger in the masala spices ? {"Cinnamom" in masala_spices}")
