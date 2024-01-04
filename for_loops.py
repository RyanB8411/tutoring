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
    
fruits = ['apple', 'orange', 'strawberry', 'banana', 'kiwi', 'banana']
count = 0
indexes = []
lettera = 0

for fruit in fruits:#fruit is an imaginary object you are using to assign a temporary variable 
    count += 1
    if fruit == 'banana':
        indexes.append(count)
        if len(indexes) == 1:
            for a in fruit:
                if a == 'a':
                    lettera += 1
        continue
    
print('banana is the', *indexes, 'element in your list')
print('there are', lettera, 'a\'s in banana')

list2 = list(filter(lambda name: name == 'banana', fruits))
print(len(list2))

