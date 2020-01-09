import operator
import os.path
# czy funkcje zawsze muszą coś zwracać?
# czy zawsze potrzebujemy zamykć pliki jak je otwieramy?

inventory = {
    "dagger": 2,
    "axe": 1,
    "crossbow": 3
}

def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    for key in inventory:
        print(key + ": " + str(inventory[key]))


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if item in inventory:
            if inventory[item] == 1:
                del inventory[item]
            else:
                inventory[item] -= 1


def sort_inventory_items(inventory, order="count,desc"):
    """Sorts the inventory dictionary in ascending or descending order. Returns sorted_inventory as a list."""
    if order == "count,desc":
        sorted_inventory_list = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)
    elif order == "count,asc":
        sorted_inventory_list = sorted(inventory.items(), key=operator.itemgetter(1))
    else:
        sorted_inventory_list = list(inventory.items())
    return sorted_inventory_list


def set_table_width(inventory, headers):
    """ Defines a width of columns so the table fits to the longest elements.""" 
    name_width = len(headers[0])
    for name, count in inventory:
        if len(name) > name_width:
            name_width = len(name)

    count_width = len(headers[1])
    for name, count in inventory:
        if len(str(count)) > count_width:
            count_width = len(str(count))

    return (name_width, count_width)

def print_table(inventory, order="unordered"):
    """Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    The "order" parameters can be: "unordered" (default), "count,desc" and "count,asc"."""

    headers = ("item name", "count")
    inventory_to_print = sort_inventory_items(inventory, order)
    name_width, count_width = set_table_width(inventory_to_print, headers)
    vertical_break = " | "
    total_width = name_width + len(vertical_break) + count_width
    
    print((total_width) * "-")
    print(f"{headers[0]:>{name_width}}{vertical_break}{headers[1]:>{count_width}}")
    print((total_width) * "-")

    for name, count in inventory_to_print:
        print(f"{name:>{name_width}}{vertical_break}{count:>{count_width}}")
    
    print((total_width) * "-")


def import_inventory(inventory, filename="import_inventory.csv"):
    """Import new inventory items from a CSV file.""" 
    try:
        file_to_import = open(filename, "r")
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    else:
        file_content = file_to_import.read()
        elements_to_import = file_content.split(',')
        add_to_inventory(inventory, elements_to_import)


def export_inventory(inventory, filename="export_inventory.csv"):
    """Export the inventory into a CSV file."""
    try:
        file_to_export_to = open(filename, "w+")
    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")
    else:
        list_to_export = []
        for key, value in inventory.items():
            for i in range(value):
                list_to_export.append(key)
        string_to_export = ",".join(list_to_export)
        file_to_export_to.write(string_to_export)