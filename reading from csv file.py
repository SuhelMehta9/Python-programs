import csv
import sys
def read_from_file(filename):
    with open(filename, 'r') as myfile:
        content = list(csv.reader(myfile))
        for rows in content:
            print(', '.join(rows))
    return
filename = input('Enter the name of file: ')
try:
    read_from_file(filename)
    
except FileNotFoundError:
    print('Please check name of file again')
