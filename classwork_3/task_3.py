def print_stars(num_stars):
    if num_stars == 0:
        return
    else:
        print("*", end="")
        print_stars(num_stars - 1)


num_stars = int(input("Please enter amount of stars: "))


print_stars(num_stars)
