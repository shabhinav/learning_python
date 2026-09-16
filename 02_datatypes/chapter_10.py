
chai_order = dict(type="Masala Chai",size="Large",sugar=2)
print(f"Chai order {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"


print(f"Recipe base: {chai_recipe['base']}")
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

#membership test
# print(f"Is sugar exist? {'sugar' in chai_order}")
chai_order = {
    "type":"Ginger Chai",
    "size":"Medium",
    "sugar":1
}

# print(f"order details (keys) {chai_order.keys()}")
# print(f"order details (values) {chai_order.values()}")
# print(f"order details (items) {chai_order.items()}")


last_item = chai_order.popitem()

print(f"Remove last item {last_item} {chai_order}")

extra_spices = {
    "cardamom": "crushed",
    "ginger": "slices"
}

chai_recipe.update(extra_spices)

print(f"Updated Chai Recipe {chai_recipe}")

chai_size = chai_order.get("size","No keys exist")

print(f"chai_size {chai_size}")



