import json
from Task6.gen_random import gen_random
from Task6.print_result import print_result
from Task6.unique import Unique
from Task6.cm_timer import cm_timer_1
from Task6.field import field

# Сделаем другие необходимые импорты


path = "C:/Lab3/data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк
with open(path, encoding='utf8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(Unique(list(field(arg, 'job-name')), ignore_case=True)), key=lambda x: str.casefold(x))


@print_result
def f2(arg):
    return list(filter(lambda x: "программист" in x.lower(), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return dict(zip(arg, gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
        # f1(data)
