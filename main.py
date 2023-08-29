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