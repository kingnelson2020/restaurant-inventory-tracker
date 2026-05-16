""" Module that handles how the inventory is displayed """

def display_inventory(inventory_list):
    """ Loop through the List and the dictionary of items
        Args: Take theinventory list
        Return: A proper display of all items in the inventory
    """
    print('=============== CURRENT INVENTORY ====================')
    for index, item_dict in enumerate(inventory_list, start=1):
        #separate all dictionaries in the list
        print(f'{index}. {item_dict['item']}')
        
        print(f'   Quantity        : {item_dict['quantity']}')
        print(f'   Unit            : {item_dict['unit']}')
        print(f'   Reorder Level   : {item_dict['reorder_level']}')
        print('--------------------------------------------------')
            
    