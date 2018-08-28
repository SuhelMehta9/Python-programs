
# coding: utf-8

# In[7]:


filename = 'abberivations.txt' # Storing the name of file in variable 
usrInput = input('Enter message here\n>> ').lower() # Taking input from user
usrInput_list = usrInput.split() # Converting the user input(usrInput) to list(usrInput_list) with refrence to white space
filename = open(filename, 'r') # Opening the file
content = filename.read() # Reading the content
fileContent=content.split('\n') # Converting content into list

for word in usrInput_list:
    index = usrInput_list.index(word)
    if word in fileContent: # Finding usrInput_list content in fileContent
        if word != 'hello':
            index2 = fileContent.index(word)
            usrInput_list[index] = fileContent[(index2)+1] # Updating the value
output = str(' '.join(usrInput_list)) # Converting the list into string 
print(output.capitalize()) # Capitalizing the string

