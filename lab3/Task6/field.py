"""Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}"""
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]


def field(items, *args):
            assert len(args) > 0
            if len(args) == 1:
                for dic in items:
                    for arg in args:
                        if arg in dic:
                            yield dic[arg]
            else:
                for dic in items:
                    new_item = {}
                    for arg in args:
                        if arg in dic:
                                new_item[arg] = dic[arg]
                    if len(new_item.keys()) > 0:
                        yield new_item


def main():
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))
    print(list(field(goods, 'title', 'price', 'color')))


if __name__ == "__main__":
    main()
