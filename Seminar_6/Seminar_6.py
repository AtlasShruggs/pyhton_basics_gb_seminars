from functools import reduce

try:
    ex_num = int(input('Введи номер задачи: '))
except:
    print('Такой задачи нет. Попробуй еще раз')


if ex_num == 1:
    num_list = [int(i) for i in input('Введи целые числа через пробел: ').split()]

    two_digits_list = filter(lambda x: x // 10 and not x // 100, num_list)

    print(*two_digits_list, sep=' ')

if ex_num == 2:

    work_list = [i for i in input('Введи разные штуки через пробел: ').split()]

    digits = filter(lambda x: x.isdigit(), work_list)

    letters = filter(lambda x: x.isalpha(), work_list)

    digits, letters = list(map(list,(digits, letters)))

    combined = [el for el in work_list if el not in digits+letters]

    


    print(*letters)
    print(*digits)
    print(*combined)

