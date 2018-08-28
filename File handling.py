# This program is to write to a file while the user want.
WRITE = 'w'
READ = 'r'
APPEND = 'a+'
filename = 'csvfile.csv'
answer = input('Do you want to write a file?(y/n): ')
if answer == 'y':
    
    while answer == 'y':
        file = open(filename, mode = APPEND)
        file.write(("\n"))
        file.write(input('Start typing: \n'))
        answer = input('Do you want to write file again?(y/n): ').lower()
        file.close()
else:
    print('Exiting')
