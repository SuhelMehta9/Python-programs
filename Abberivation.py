# Some do not understand the abberviations like LOL etc. so to make it easy to read for them this program takes whole message and return
# the full message.

filename = 'abberivations.txt' # Storing the name of file in variable 
usrInput = input('Enter message here\n>> ').lower() # Taking input from user
usrInput_list = usrInput.split() # Converting the user input(usrInput) to list(usrInput_list) with refrence to white space
filename = open(filename, 'r') # Opening the file
content = filename.read() # Reading the content
fileContent=content.split('\n') # Converting content into list

for word in usrInput_list:
    index = usrInput_list.index(word)
    if word in fileContent: # Finding usrInput_list content in fileContent
        if word != 'hello': # hello is also in file so inorder to ignore this type of change this code is added
            index2 = fileContent.index(word)
            usrInput_list[index] = fileContent[(index2)+1] # Updating the value
output = str(' '.join(usrInput_list)) # Converting the list into string 
print(output.capitalize()) # Capitalizing the string

