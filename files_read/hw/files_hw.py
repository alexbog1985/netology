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


def add_ingredient(list_recipe):
    recipes = {}
    ingredient_list = []
    for recipe in list_recipe:
        recipe_name = recipe[0]
        for item in recipe[2:]:
            ingredients = {'ingredient_name': item.split('|')[0],
                           'quantity': item.split('|')[1],
                           'measure': item.split('|')[2]}
            ingredient_list.append(ingredients)
        recipes[recipe_name] = ingredient_list
        ingredient_list = []
    return recipes


print(get_list_recipes('recipes.txt'))
print(add_ingredient(get_list_recipes('recipes.txt')))
