month_number= int(input("enter month number here (1-12): "))
match month_number:
    case 1:
        print("january")
    case 2:
        print("febuary")
    case 3:
        print("march")
    case 4:
        print("april")
    case 5:
        print("may")
    case 6:
        print("june")
    case 7:
        print("july")
    case 8:
        print("augest")
    case 9:
        print("september")
    case 10:
        print("october")
    case 11:
        print("november")
    case 12:
        print("december")
    case _:
        print("invalid number")