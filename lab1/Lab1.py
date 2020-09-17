import argparse
print('Лабораторная работа №1', end='\n')
print('Выполнил студент:Ли М.В. Группа:ИУ5-54Б', end='\n')
complete = 'y'
parser = argparse.ArgumentParser()
parser.add_argument("--a", help="Коэффициент А Биквадратного уравнения", type=float)
parser.add_argument("--b", help="Коэффициент B Биквадратного уравнения", type=float)
parser.add_argument("--c", help="Коэффициент C Биквадратного уравнения", type=float)
args = parser.parse_args()
while complete == 'y':
    a = args.a
    b = args.b
    c = args.c
    if a == None and b == None and c == None:
        a = input('Введите значение первого аругмента: ')
        b = input('Введите значение второго аргумента: ')
        c = input('Введите значение третьего аргумента: ')
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:  # Проверка на ошибку неверного формата (введены буквы)
        print('Введены некорректные символы, повторите ввод.')
    else:
        discriminant = b ** 2 - 4 * a * c
        if a==0 and b==0 and c==0:
            print("Коэффициент a и b не может быть равен нулю. Если a=0 b=0, то уравнение будет линейным (не квадратным). ")
        elif a==0:
            if c < 0:
                answer = pow(-c / b, 0.5)
                print('x1 = ' + str(answer))
                print('x2 = ' + str(-answer))
            elif c == 0:
                print("x = 0")
            else:
                print("\033[31mКорней нет!\033[0m")
        else:
            if discriminant < 0:
                print('Действительных корней нет')
            elif discriminant == 0:
                x = -b / (2 * a)
                print('x1 = ' + str(x ** 0.5))
                print('x2 = ' + str(-x ** 0.5))
            else:
                x1 = (-b + discriminant ** 0.5) / (2 * a)
                x2 = (-b - discriminant ** 0.5) / (2 * a)

                if x1<0 and x2<0:
                    print("Корней нет")
                elif x1>0 and x2<0:
                    answer1 = x1**0.5
                    answer2 = -x1 ** 0.5
                    print('Корнями уравнения являются:')
                    print('x1 = ' + str(answer1))
                    print('x2 = ' + str(answer2))
                elif x1<0 and x2>0:
                    answer1 = x2 ** 0.5
                    answer2 = -x2 ** 0.5
                    print('Корнями уравнения являются:')
                    print('x1 = ' + str(answer1))
                    print('x2 = ' + str(answer2))
                else:
                    answer1 = x1**0.5
                    answer2 = -x1 ** 0.5
                    answer3 = x2 ** 0.5
                    answer4 = -x2 ** 0.5
                    print('Корнями уравнения являются:')
                    print('x1 = ' + str(answer1))
                    print('x2 = ' + str(answer2))
                    print('x3 = ' + str(answer3))
                    print('x4 = ' + str(answer4))
    print('Чтобы продолжить введите "y", для выхода введите любой символ.')
    complete = input()
else:
    print('Выход из программы')
    exit()
