try:
    ex_num = int(input('Введите номер задачи '))

    if ex_num == 1:

        try:
            lst = [float(i) for i in input('Введите массив чисел через пробел: ').split()]

            summary = 0
            for i in range(1, len(lst), 2):
                summary += lst[i]

            print(f'Сумма нечетных элементов массива равна {summary}')
        except:
            print('Числа. Через. Пробел!')

    if ex_num == 2:

        try:
            lst = [float(i) for i in input('Введите массив чисел через пробел: ').split()]

            new_lst = []

            for i, el in enumerate(lst):
                if i >= len(lst) / 2:
                    break
                else:
                    new_lst.append(el * lst[len(lst)-1-i])
            print(*new_lst)
        except:
            print('Числа. Через. Пробел!')

    if ex_num == 3:

        try:
            lst = [float(i) for i in input('Введите массив чисел через пробел: ').split()]

            parts = [str(i).split('.')[1] for i  in lst ]

            parts_max_len = len(max(parts, key=len))

            parts_int = []
            for el in parts:
                parts_int.append(int(el + '0' * (parts_max_len - len(el))))
        
            diff = float('0.' + str(max(parts_int) - min(parts_int)))
            print(diff)


        except:
            print('Числа. Через. Пробел!')








except:
    print('Задачи с таким номером нет. Попробуйте позднее')