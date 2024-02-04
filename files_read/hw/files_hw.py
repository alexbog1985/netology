def get_list_recipes(file):
    with open(file, 'r', encoding='utf8') as f:
        text_file = ''
        for line in f:
            text_file += line
        file_list = text_file.split('\n\n')
        recipe_list = []
        for recipe in file_list:
            recipes = recipe.split('\n')
            recipe_list.append(recipes)
    return recipe_list


def add_cook_book(list_recipe):
    recipes = {}
    ingredient_list = []
    for recipe in list_recipe:
        recipe_name = recipe[0]
        for item in recipe[2:]:
            ingredients = {'ingredient_name': item.split(' | ')[0],
                           'quantity': item.split(' | ')[1],
                           'measure': item.split(' | ')[2]}
            ingredient_list.append(ingredients)
        recipes[recipe_name] = ingredient_list
        ingredient_list = []
    return recipes


def get_shop_list_by_dishes(dishes, person_count=1):
    cook_book = add_cook_book(get_list_recipes('recipes.txt'))
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for item in cook_book[dish]:
                if item['ingredient_name'] not in shop_list.keys():
                    shop_list[item['ingredient_name']] = {'measure': item['measure'],
                                                          'quantity': int(item['quantity']) * person_count}
                else:
                    shop_list[item['ingredient_name']]['quantity'] += (int(item['quantity']) * person_count)
        else:
            print(f'В кулинарной книге нет рецепта {dish}')
    return dict(sorted(shop_list.items()))


print(add_cook_book(get_list_recipes('recipes.txt')))
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
