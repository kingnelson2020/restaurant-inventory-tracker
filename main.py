from src.user_input import get_new_inventory
from src.inventory import add_inventory

def main():
    
    print('===================================================')
    print('--------Restaurant Inventory Tracker v1.0 ---------')
    print('===================================================')
    
    inventory = []
    
    while True:
        print('1. Add new inventory')
        print('2. View inventory')
        print('3. Exit')
        try:
            
            user_choice = int(input('\nEnter your choice: '))
            
            if user_choice == 1:
                new_inventory = get_new_inventory()
                add_inventory(inventory, new_inventory)
            elif user_choice == 2:
                print(inventory)
            elif user_choice == 3:
                break
            else:
                print('Please choose between 1 - 3')
                
        except ValueError:
            print('Wrong selection! You must select numbers between 1 - 3')





if __name__ == "__main__":
    main()