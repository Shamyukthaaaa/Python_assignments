#LIST METHODS [To Be Implemented]
colors=[]
num=int(input("Enter the number of elements to be added in the list: "))
for i in range(num):
    color=input("Enter the color {} to be added in the list: ".format(i+1))
    colors.append(color)
print(colors)

#append method
colors.append("Brown")
print(colors)
#insert method
colors.insert(3,"Grey")
print(colors)
#copy method
colors_copy=[]
colors_copy=colors.copy()
print(colors_copy)
#index method
colors.index("Orange")
#join method
fruits=["apple","mango","papaya"]
new_list=colors+fruits
print(new_list)
#concatenation
colors=colors*2
print(colors)
#sort method
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
#len method
print(len(colors))
#max method
print(max(colors))
#min method
print(min(colors))
#reverse method
colors.reverse()
print(colors)
#extend method
print(fruits.extend(colors))
#count method
print(colors.count("Orange"))
#pop method
colors.pop([2])
print(colors)
colors.pop()
print(colors)
#remove method
colors.remove("Black")
print(colors)
#clear method
colors.clear()
print(colors)
#delete method
del colors["Brown"]
del fruits
print(colors)
print(fruits)
    
