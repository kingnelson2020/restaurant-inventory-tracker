import csv
import os

STORAGE_FILE = 'restaurant_inventory.csv'
FIELDNAMES = ['item', 'quantity', 'unit', 'reorder_level']


def load_from_csv() -> list[dict]:
    """ Initialization and data hydration
        Checks if storage file exists. If it doesn't, return an empty state.
        If it does, load rows and explicitly cast strings back to numerical type.
    """
    if not os.path.exists(STORAGE_FILE):
        print('[Initialization] No storage file found. Starting a clean slate.')
        return []
    inventory_list = []
    try:
        with open(STORAGE_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['quantity'] = int(row['quantity'])
                    row['reorder_level'] = int(row['reorder_level'])
                    
                    inventory_list.append(row)
                
                except (ValueError, TypeError) as row_err:
                    print(f"Skipping corrupted row for item '{row.get('item', 'unknown')}': {row_err}")
                    
        print(f'Successfully loaded {len(inventory_list)} records.')
        return inventory_list
        
    except Exception as e:
        print(f'[Error] Failed to read storage files: {e}. Starting a clean slate')
        return []
    

def save_to_csv(inventory_list: list[dict]) -> None:
    """ Overwrite the CSV file with the current memory state. """
    try:
        with open(STORAGE_FILE, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(inventory_list)
        print('Application state successfully saved.')
        
    except IOError as e:
        print(f'[Error] Critical: Could not write data to file: {e}')