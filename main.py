from src.user_input import get_new_inventory, get_update_input
from src.inventory import add_inventory, update_quantity
from src.views import display_inventory

def main():
    
    print('===================================================')
    print('--------Restaurant Inventory Tracker v1.0 ---------')
    print('===================================================')
    
    inventory = []
    
    while True:
        print('\n1. Add new inventory')
        print('2. View inventory')
        print('3. Update quantity')
        print('4. Exit')
        try:
            
            user_choice = int(input('\nEnter your choice: '))
            
            if user_choice == 1:
                new_inventory = get_new_inventory()
                add_inventory(inventory, new_inventory)
            elif user_choice == 2:
                if inventory != []:
                    display_inventory(inventory)
                else:
                    print('The inventory is empty.')
            elif user_choice == 3:
                target_name, new_qty = get_update_input()
                success = update_quantity(inventory, target_name, new_qty)
                if success:
                    print(f'Success: Updated {target_name.capitalize()} quantity to {new_qty}.')
                else:
                    print(f'Error: {target_name.capitalize()} was not found in inventory.')
            elif user_choice == 4:
                break
            else:
                print('Please choose between 1 - 4')
                
        except ValueError:
            print(f'{ValueError}')





if __name__ == "__main__":
    main()