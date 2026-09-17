seat_type = input("Entyer the seat type (SLEEPER/AC/GENERAL/LUXURY):").lower()

match seat_type:
    case "sleeper":
        print("SLEEPER TYPE")
    case "ac":
        print("ac TYPE")
    case "general":
        print("general type")
    case "luxury":
        print("luxury type")
    case _:
        print("No seat type avail")