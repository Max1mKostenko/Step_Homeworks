user_num = int(input("Please enter some four digit number: "))

if len(str(user_num)) == 4:
    nums = [user_num // 1000, user_num // 100 % 10, user_num % 100 // 10, user_num % 10]

    print(f"Reversed number to {user_num} is {nums[-1] * 1000 + nums[-2] * 100 + nums[-3] * 10 + nums[0]}")
else:
    print("Your input isn't four digit number!")
