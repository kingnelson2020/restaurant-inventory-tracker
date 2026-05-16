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
                print('Add new inventory')
            elif user_choice == 2:
                print('View inventory')
            elif user_choice == 3:
                break
            else:
                print('Please choose between 1 - 3')
                
        except ValueError:
            print('Wrong selection! You must select numbers between 1 - 3')





if __name__ == "__main__":
    main()