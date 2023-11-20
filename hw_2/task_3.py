meters = float(input("Please enter any count of meters: "))

if meters > 0:
    print(f"{meters} meters in centimeters is: {meters * 100}")
    print(f"{meters} meters in decimeters is:  {meters * 10}")
    print(f"{meters} meters in millimeters is: {meters * 1000}")
    print(f"{meters} meters in miles is:       {round(meters * 0.00062137, 3)}")
else:
    print("Number should be positive!")
