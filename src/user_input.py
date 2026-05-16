""" Module for taking User input """
def get_new_inventory():
    """ Collect Inventory Items from the User.
        Returns a dictionary{name, quantity, unit, reorder_level}
    """
    item = input('Item: ')
    
    quantity = int(input('Quantity: '))
    unit = input('Unit: ')
    reorder_level = int(input('Reorder level: '))
        
    
    return {
        'item': item,
        'quantity': quantity,
        'unit': unit,
        'reorder_level': reorder_level
    }