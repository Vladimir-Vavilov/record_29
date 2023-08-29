from pprint import pprint
with open('reception.txt', 'rt') as f:
    cook_book = {}
    for line in f:
        eat_name = line.strip()
        ingredient_name = int(f.readline())
        meas = []
        for i in range(ingredient_name):
            mea = f.readline()
            ingredient, quantity, measure = mea.split(' | ')
            meas.append({
                'ingredient_name': ingredient,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[eat_name] = meas
pprint(cook_book)

def my_cook_book():
    with open('reception.txt', encoding='utf-8') as file:
        cook_book = {}
        for txt in file.read().split('\n\n'):
            name, _, *args = txt.split('\n')
            tmp = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = tmp
    return cook_book
def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')

    shop_list = get_shop_list_by_dishes(dishes, person_count)

    return (shop_list)
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in my_cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']


    return shop_list



create_shop_list()

get_shop_list_by_dishes()

