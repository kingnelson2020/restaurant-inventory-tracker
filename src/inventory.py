""" Module for performing Inventory Operations """

def add_inventory(inventory_list, new_inventory):
    """ Add the new inventory item to the existing inventory 
        Args: Inventory and the new inventory
        Returns: An updated inventory lists.
    """
    inventory_list.append(new_inventory)
    
    print('Item added successfully\n')
    
    return inventory_list