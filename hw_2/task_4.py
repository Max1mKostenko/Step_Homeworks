height = float(input("Please enter height of triangle: "))
side = float(input("Please enter side of triangle: "))

if height > 0:
    if side > 0:
        print(f"Square of triangle = 1/2 * height({height}) * side({side}) = {0.5 * height * side}")
    else:
        print("Side of triangle can't be less than zero.")
else:
    print("Height of triangle can't be less than zero.")
