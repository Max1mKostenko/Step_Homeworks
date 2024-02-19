def describe_person(**info):
    for a, b in info.items():
        print(f"{a}: {b}")


describe_person(name="Maxim", surname="Kostenko", age=15)
