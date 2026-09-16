chai_type = "Ginger chai"
customer_name = "Priya"


print(f"Order for {customer_name} : {chai_type} please!")


chai_description = "Aromatic and Bold"

print(f"First Word: {chai_description[:8]}")
print(f"Last Word: {chai_description[12:]}")
print(f"reverse String: {chai_description[::-1]}") # reverse the string "dloB dna citamorA"

label_text = "chai spÉcial"
ecoded_label = label_text.encode("utf-8")
decoded_label = ecoded_label.decode("utf-8")

print(f"Encode label: {ecoded_label}")
print(f"Non Encode label: {label_text}")
print(f"dencode label: {decoded_label}")

