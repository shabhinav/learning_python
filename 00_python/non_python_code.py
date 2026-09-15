def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("tea_leaves")
    add_to_cup("sugar")
    add_to_cup("boilded water")
    add_to_cup("cup")
    add_to_cup("chay=i")
