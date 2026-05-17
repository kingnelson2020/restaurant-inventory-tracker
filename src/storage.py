import csv
import os

STORAGE_FILE = 'restaurant_inventory.csv'
FIELDNAMES = ['item', 'quantity', 'unit', 'reorder_level']




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