books=dict()
num=int(input("Enter the number of items to be added: "))
for i in range(num):
    animals[input("Enter book {}: ".format(i+1))]=input("Enter author {}: ".format(i+1))
print(animals)
#update method
books.update({'Wings of Fire':'A.P.J. Abdul Kalam'})
print(books)
#copy method
books_copy=books.copy()
print(books_copy)
#keys method
animals.keys()
print(books)
#values method
books.values()
print(books)
#items method
books.items()
print(books)
#get method
print(books.get('David Copperfield'))
#pop method
books.pop('Madame Bovary')
print(books)
#popitem method
print(books.popitem())
#setdefault
books.setdefault('Panchathantra','Vishnu Sharma')
#remove method
books.remove('War and Peace')
#del method
del books['Pride and Prejudice']
#clear method
books.clear()
print(books)
#del method
del books
