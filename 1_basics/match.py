day="Monday"
match day:
    case "Sunday":
        print("The day is Sunday")
    case "Monday":
        print("The day is Monday")
    case "Friday":
        print("The day is Friday")
        print("The last working day")
    case _:
        print("NOt valid day entered")
        
