""" Module for taking User input """
from src.utils import get_valid_string, get_valid_int
def get_new_inventory():
    """ Collect Inventory Items from the User.
        Returns a dictionary{name, quantity, unit, reorder_level}
    """
    item = get_valid_string('Item: ')
    quantity = get_valid_int('Quantity: ')
    unit = input('Unit: ').strip()
    reorder_level = get_valid_int('Reorder level: ')
        
    
    return {
        'item': item,
        'quantity': quantity,
        'unit': unit,
        'reorder_level': reorder_level
    }