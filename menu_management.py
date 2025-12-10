def addItem(menu, item):
    if item in menu:
        return f'Item "{item}" already exists in the menu, {menu}'
    menu.append(item)
    return f'Updated Menu: {menu}'

def removeItem(menu, item):
    if item not in menu:
        return f'Item "{item}" does not exist in the menu, {menu}'
    menu.remove(item)
    return f'Updated Menu: {menu}'

def checkItem(menu, item):
    return f'Availability: "{item} is {"available" if item in menu else "not available"}"'

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

print(addItem(initial_menu, "Sushi"))
print(removeItem(initial_menu, "Pasta"))
print(checkItem(initial_menu, "Burger"))