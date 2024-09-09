my_shopping_list = ['bread', 'milk', 'butter']

print(my_shopping_list[0],my_shopping_list)

print(len(my_shopping_list))


def bring_more_food(my_list):
    more_item = input("enter the item\n")
    my_list.append(more_item)
    return my_list
l = bring_more_food((my_shopping_list))

print(l)
