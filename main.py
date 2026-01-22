try:
    x = int(input("Введите число: "))
    y = int(input("Введите второе число: "))
    z = str(input('Введите действие: '))

    if z == '+':
        print(x + y)

    elif z == '-':
        print(x - y)

    elif z == '*':
        print(x * y)

    elif z == '/':
        print(x / y)
    else:
        print("Вы ввели неверную операцию.")
except ValueError:
    print("Вы ввели некорректный тип данных либо это не число.")
except ZeroDivisionError:
    print("На ноль делить нельзя.")
