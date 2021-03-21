import os
import glob


def file_delete(folder, file):
    lst = glob.glob(f'/Users/Tahmid Bhuiyan/{folder}/{file}')
    for path in lst:
        print(path)
    y_or_n = input('\nThese are the identified files. Proceed with deletion? Answer with "Y" or "N" ').lower()

    if y_or_n == 'Y':
        for path in lst:
            new_path = path.replace('/', '\\')
            os.remove(new_path)
    else:
        return None


while True:
    path_destination = input('Where would you like to delete files from? ')
    fileName = input('Unix pattern rules:\n* for any characters before, after, or in between\nName of file? ')
    file_delete(path_destination, fileName)

    proceed = input('Continue deleting files? Answer with "Y" or "N" ').lower()
    if proceed == 'n':
        break

