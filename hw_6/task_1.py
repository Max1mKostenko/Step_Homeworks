from variables import a, b, c, d, e, f, g, h, i, j

while True:
    inp = input("\nPlease enter any number in the range from 0 to 10 (enter 0 to exit): ")

    if inp == "0":
        print("Exiting the program.")
        break

    elif int(inp) in range(1, 11):
        k = {"1": a, "2": b, "3": c,
             "4": d, "5": e, "6": f,
             "7": g, "8": h, "9": i, "10": j}
        print(k[f"{inp}"])

    else:
        print("\nYour input isn't correct. Please enter a number between 0 and 10.")
