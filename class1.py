#creating Dog class
class Dog:
    #class attribute
    species="Canis lupus familiaris"
    #instance attributes
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed

    def speak(self,sound):
        return f"{self.name} says {sound}"

#Dog object is created and stored in variable dog1,dog2,dog3 respectively
dog1=Dog("Mille",4,"German Shepherd")
dog2=Dog("Snowy",6,"Bulldog")
dog3=Dog("Rosy",5,"Poddle")

#accessing attributes of objects using dot operator
print(dog1.name,dog1.age,dog1.breed,dog1.species)
print(dog2.name,dog2.age,dog2.breed,dog2.species)
print(dog3.name,dog3.age,dog3.breed,dog3.species)

#changing values dynamically
dog1.age=5
print(dog1.age)
print(dog1.speak("bow bow"))

#creating car class

class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
        

car1=Car("blue",20000)
car2=Car("red",30000)
print("The",car1.color, "has", car1.mileage, "miles")
print("The",car2.color, "has", car2.mileage,"miles")



