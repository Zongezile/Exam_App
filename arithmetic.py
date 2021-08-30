import random

mark = 0

while True:
    try:
        level = int(input('''Which level do you want? Enter a number:
        1 - simple operations with numbers 2-9
        2 - integral squares of 11-29 \n'''))

        if level in [1, 2]:
            break

    except (ValueError, TypeError):
        print("Incorrect format.")

if level == 1:
    level_description = 'simple operations with numbers 2-9'
    for x in range(5):
        number_1 = random.randint(2, 9)
        sign = random.choice('+-*')
        number_2 = random.randint(2, 9)
        print(number_1, sign, number_2)

        if sign == "+":
            real_result = number_1 + number_2
        elif sign == "-":
            real_result = number_1 - number_2
        elif sign == "*":
            real_result = number_1 * number_2

        while True:
            try:
                result = input()
                if int(result) == real_result:
                    print("Right!")
                    mark += 1
                    break
                else:
                    print("Wrong!")
                    break

            except (ValueError, TypeError):
                print("Incorrect format.")
else:
    level_description = 'integral squares of 11-29'
    for x in range(5):
        number = random.randint(11, 29)
        print(number)
        real_result = number * number

        while True:
            try:
                result = input()
                if int(result) == real_result:
                    print("Right!")
                    mark += 1
                    break
                else:
                    print("Wrong!")
                    break

            except (ValueError, TypeError):
                print("Incorrect format.")

save = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")

if save in ['yes', 'YES', 'y', 'Yes']:
    name = input("What is your name?")
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(f'{name}: {mark}/5 in level {level} ({level_description}).')
    file.close()
    print('The results are saved in "results.txt".')
else:
    quit()