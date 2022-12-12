from functools import reduce

try:
    ex_num = int(input('Введи номер задачи: '))

    if ex_num == 1:
        num_list = [int(i) for i in input('Введи целые числа через пробел: ').split()]

    two_digits_list = filter(lambda x: x // 10 and not x // 100, num_list)

    print(*two_digits_list, sep=' ')

except:
    print('Такой задачи нет. Попробуй еще раз')