""" Module for taking User input """
def get_new_inventory():
    """ Collect Inventory Items from the User.
        Returns a dictionary{name, quantity, unit, reorder_level}
    """
    item_name = input('Item name: ')
    quantity = int(input('Quantity: '))
    unit = input('Unit: ')
    reorder_level = input('Reorder level: ')
        
    
    return {
        'item_name': item_name,
        'quantity': quantity,
        'unit': unit,
        'reorder_level': reorder_level
    }