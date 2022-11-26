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

    if ex_num == 4:
        try:
            n = int(input('Введите целое число N: '))
            
            sign=''

            if n < 0:
                sign = str(n)[0]
                n *= -1
            
            binary = ''


            while n >= 1:
                binary += str(n % 2)
                n = n // 2

            binary = sign + binary[::-1]

            print(f'Двоичное представление числа {n} = {binary}')



        except:
            print('Целое число!')

    if ex_num == 5:

        def fibonacci(n):
            lst = [0, 1]
            x1, x2 = 0,1    
            for i in range(n-1):
                x1, x2 = x2, x1 + x2
                lst.append(x2)
            
            return lst 
        
        try:
            k = int(input('Введите кол-во членов последовательности Фибоначчи: '))
            pos_fib = fibonacci(k)
            neg_fib_temp = fibonacci(k)[1:]

            neg_fib_permanent = []
            for i, el in enumerate(neg_fib_temp):
                neg_fib_permanent.append(el * (-1) ** i)

            seq = neg_fib_permanent[::-1] + pos_fib

            print(*seq, sep=' ')

        except:
            print('Опять вы накосячили :(')







except:
    print('Задачи с таким номером нет. Попробуйте позднее')