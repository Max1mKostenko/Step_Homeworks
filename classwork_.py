print("*" * int(input("Please enter length of line: ")))

symbol = input("PLease enter any symbol to make line: ")

if len(symbol) == 1:
    print(symbol * int(input("Please enter length of line: ")))
else:
    print("You must enter only one symbol.")
