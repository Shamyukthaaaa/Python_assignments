#To Be Implemented methods on tuple
numbers=[]
num=int(input("Enter the number of elements to be added in tuple: "))
for i in range(num):
    elements=int(input("Enter element {} ".format(i+1)))
    numbers.append(elements)
print(tuple(numbers))

#index method
print(numbers.index(3))
#len method
print(len(numbers))
#count method
print(numbers.count(1))
#max method
print(max(numbers))
#min method
print(min(numbers))
#delete method
del numbers
