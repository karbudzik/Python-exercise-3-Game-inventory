import operator
# czy funkcje muszą coś zwracać?

inventory = {
    "dagger": 2,
    "axe": 1,
    "crossbow": 33
}
empty_inventory = {}

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
    """
    Display the contents of the inventory in an ordered, well-organized table with
    each column right-aligned.
    The "order" parameters can be: "unordered" (default), "count,desc" and "count,asc".
    """
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

# Write a function named import_inventory(inventory, filename) which can import new inventory items from a CSV file.

#     The function can handle CSV files containing items in the following format: ruby,rope,ruby,gold coin,ruby,axe
#     Calling the function with a dictionary and items in a file in comma separated format (e.g. rope, torch, arrow) 
#     which aren't in the inventory yet results in that the items are added to the inventory as keys and values are set to 1
#     Calling the function with a dictionary and items in a CSV file which are already in the inventory results in that those 
#     items' value are incremented by 1
#     The function could handle if the CSV file contains multiple occurences of the same item, then dictionary values are 
#     incremented by the number of occurences
#     If not specified, the filename argument is by default import_inventory.csv
#     If the file provided in the filename argument cannot be reached on the disk, then the error message 
#     File '<filename>' not found! is shown on the console output

def import_inventory(inventory, filename):
    """Import new inventory items from a CSV file."""

    pass


# Write a function named export_inventory(inventory, filename) which can export all inventory items to a CSV file.

#     Calling the function with a non-empty dictionary and a filename argument results in the dictionary keys 
#     to be saved in CSV format in the file
#     If there are keys in the dictionary with values greater than 1, then the key is saved into the file as many times 
#     as the value
#     If not specified, the filename argument is by default export_inventory.csv
#     The file denoted in the filename argument is automatically created if not exists, and is overwritten if already exists
#     If the user executing the function does not have write access in the folder where the script is executed 
#     then the error message You don't have permission creating file '<filename>'! is shown on the console output

def export_inventory(inventory, filename):
    """Export the inventory into a CSV file."""

    pass
