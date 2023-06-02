while True:
    getal = int(input("Please input a number: "));
    if getal == 100:
        print("That's more like it!");
        break;
    elif getal < 100:
        print("Don't be so modest!");
    elif getal > 100:
        print("Are you overcompensating?.");