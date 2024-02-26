import random


def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    secret_number = ''.join(map(str, digits[:4]))
    return secret_number


def count_bulls_and_cows(secret_number, guess, bulls=0, cows=0, index=0):
    if index == 4:
        return bulls, cows
    if guess[index] == secret_number[index]:
        bulls += 1
    elif guess[index] in secret_number:
        cows += 1
    return count_bulls_and_cows(secret_number, guess, bulls, cows, index + 1)


def play_game(secret_number, attempts=0):
    guess = input("Введите вашу догадку (четыре цифры без пробелов): ")
    if len(guess) != 4 or not guess.isdigit():
        print("Пожалуйста, введите четыре цифры.")
        return play_game(secret_number, attempts)

    bulls, cows = count_bulls_and_cows(secret_number, guess)
    attempts += 1
    print(f"Быки: {bulls}, Коровы: {cows}")

    if bulls == 4:
        print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток.")
    else:
        return play_game(secret_number, attempts)


def main():
    print("Добро пожаловать в игру 'Быки и коровы'!")
    secret_number = generate_secret_number()
    play_game(secret_number)


if __name__ == "__main__":
    main()
