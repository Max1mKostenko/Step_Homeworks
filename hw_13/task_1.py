global_variable = 10


def modify_global_variable():
    global global_variable
    global_variable += 5


print("Значення глобальної змінної до виклику функції:", global_variable)
modify_global_variable()
print("Значення глобальної змінної після виклику функції:", global_variable)
