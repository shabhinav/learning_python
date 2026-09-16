# Integer

black_tea_grams = 14

ginger_grams = 3

total_grams = black_tea_grams + ginger_grams

print(f"Total grams of base tea is {total_grams}")

remaining_tea = black_tea_grams - ginger_grams

print(f"Total grams of remaining tea is {remaining_tea}")


milk_ltrs = 7
servings = 4

milk_per_serving = milk_ltrs / servings

print(f"Milk per serving is: {milk_per_serving}")

total_tea_bag = 7
pots = 4

bags_per_pot = total_tea_bag // pots # ignore the decimals

print(f"Milk per serving is: {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup

print(f"leftover cardomom pds: {leftover_pods}")


base_flavor_strength = 2
scale_factor = 3
powerful_flavor = base_flavor_strength ** scale_factor # 2*2*2
print(f"powerful_flavor: {powerful_flavor}")


total_tea_leaves_harvested = 1_000_000_000

print(f"total_tea_leaves_harvested: {total_tea_leaves_harvested}")
