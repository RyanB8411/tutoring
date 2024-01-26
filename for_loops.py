'''
Instructor: Ryan
Student: Nicole P
Topic for loops.
'''

#What is a for loop?
    #A for loop is used for iterating over a sequence
    
#What types of data can be used in a for loop?
    #list, tuple, dictionary, set, or string
    
#What does a for loop do?
    #execute a statement once for each item
    
#Does a for loop require indexing?
    #No it does not require indexing because you can set placeholder variables
    #this is the ''number'' in for number in numbers
    
#Lets Practice
    #Create a for loop to find the random string 'banana'


tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0

for token in tokens:
    if token[0] == '<':
        token[0] == '!'
        print(token[0])
        if token[-1] == '>':
            count += 1
    else:
        continue

print(count)



#Problem 1

"""
items = ['first thing', 'second thing']

html_str = "<ul>\n"

for item in items:
    
    html_str += "<li>{}</li>\n".format(item)
    
html_str += "<ul>"

print(html_str)
"""




"""
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

usernames = []

for i in names:
    
    usernames.append(i.lower().replace(" ", "_"))
    
print(usernames, names)
"""