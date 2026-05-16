""" Module for performing Inventory Operations """
from src.utils import get_valid_int

def add_inventory(inventory_list, new_inventory):
    """ Add the new inventory item to the existing inventory 
        Args: Inventory and the new inventory
        Returns: An updated inventory lists.
    """
    inventory_list.append(new_inventory)
    
    print('Item added successfully\n')
    
    return inventory_list

def update_quantity(inventory_list, target_name, qty):
    """ Update quantity by search the inventory list using the item_name """  
    for item_dict in inventory_list:
        name = item_dict.get('item')
        
        if name.lower() == target_name.lower():
            item_dict['quantity'] = qty
            return True
    return False
            
def delete_item(inventory_list, target_name):
    """ Delete an entire dictionary by selecting the item name """
    for item_dict in inventory_list:
        name = item_dict.get('item')
        
        if name.lower() == target_name.lower():
            inventory_list.remove(item_dict)
            return True
        
    return False
            
