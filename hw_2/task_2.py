user_num = int(input("Please enter some four digit number: "))

if len(str(user_num)) == 4:
    nums = [user_num // 1000, user_num // 100 % 10, user_num % 100 // 10, user_num % 10]

    print(f"{nums[0]} * {nums[1]} * {nums[2]} * {nums[3]} = {nums[0] * nums[1] * nums[2] * nums[3]}")
else:
    print("Your input isn't four digit number!")
