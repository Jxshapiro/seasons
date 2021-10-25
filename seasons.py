month, day = input("enter date: ".lower()).split()
if month == "january" or "february":
    print("It's Winter")
if month == "march" and int(day) > 19:
    print("It's spring!!!")
elif month == "march" and int(day) < 20:
    print("It's winter!!!")
elif month == "april" or "may":
    print("It's spring!!!")
elif month == "june" and int(day) < 21:
    print("its spring")
elif month == "june" and int(day) > 20:
    print("It's summer!!!")
elif month == "july":
    print("It's summer!!!")
elif month == "august":
    print("It's summer")
elif month == "september" and int(day) < 22:
    print("It's summer!!!")
elif month == "september" and int(day) > 21:
    print("It's autumn")
elif month == "october" or "november":
    print("It's autumn")
elif month == "december" and int(day) < 20:
    print("It's autumn")
elif month == "december" and int(day) > 20:
    print("It's winter!!!")
elif month == "december" and int(day) < 21:
    print("It's autumn")
else:
    print("Invalid input")
