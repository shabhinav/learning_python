is_boiling = True # True/False;
stri_count = 5
total_actions = stri_count + is_boiling # upcasting

print(f"Total actions: {total_actions}")


milk_present = None # no milk
print(f"Is there milk? {bool(milk_present)}")


water_hot = True
tea_added = True


can_serve = water_hot and tea_added

print(f"can_serve chai: {can_serve}")

