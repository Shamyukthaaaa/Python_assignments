# To Be Implemented Set methods
fruits=set()
num=int(input("Enter the number of elements to be present in the set: "))
for i in range(num):
    fruits_set=input("Enter fruit {} :".format(i+1))
    fruits.add(fruits_set)
print(fruits)

#add method
print(fruits.add("papaya"))
#update method
veggies=["potato","ladiesfinger","beans","tomato"]
fruits.update(veggies)
print(fruits)
#len method
print(len(fruits))
#max method
print(max(fruits))
#min method
print(min(fruits))
vegetables={"tomato","carrot","yam","potato","raddish"}
#copy method
set1={}
set1=fruits.copy()
print("new set is: ",set1)
#union method
print(vegetables.union(fruits))
print(fruits.union(veggies))
#intersection method
print(fruits.intersection(vegetables))
#difference method
print(vegetables.difference(fruits))
print(fruits.difference(vegetables))
#symmetric_difference method
print(vegetables.difference_update(fruits))
print(fruits.difference_update(vegetables))
#isdisjoint method
print(fruits.isdisjoint(vegetables))
#issubset method
print(vegetables.issubset(fruits))
#issuperset method
print(fruits.issuperset(vegetables))
#pop method
fruits.pop()
print(fruits)
#remove method
fruits.remove("apple")
#discard method
vegetables.discard("tomato")
#clear method
vegetables.clear()
#del method
del fruits
