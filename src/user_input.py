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
    
def get_update_input():
    """Asks user for the item name and the new quantity."""
    target_name = get_valid_string('Enter the name of the item to update: ')
    new_qty = get_valid_int(f'Enter new quantity for {target_name}: ')
    
    return target_name, new_qty

