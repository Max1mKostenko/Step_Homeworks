def create_profile(name, surname, *hobies, **info):
    print("name:", name)
    print("surname:", surname)
    for i in hobies:
        print(f"hobies: {i}")
    for a, b in info.items():
        print(f"{a}: {b}")


create_profile("Maxim", "Kostenko", "Basketball", "Programing", age=15, city="Kherson", grade="10th")
