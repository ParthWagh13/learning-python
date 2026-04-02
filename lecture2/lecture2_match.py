house = input("Enter you name: ")

match house:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryyfindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
