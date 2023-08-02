#Return the third, fourth and fifth item
fruit = ("apple", "banana", "cherry", "orange", "melon", "mango")
print(fruit[2:5])
#Return the item from the beginning to the fourth item
print(fruit[:4])
#Return the third number to the end
print(fruit[2:])
#Check if "cherry" is present in the tuple
if "cherry" in fruit:
    print("yes, cherry is in the fruit listed")
#Convert the tuple into a list to be able to change it
x = ("apple", "orange", "banana")
y = list(x)
y[1] = ("grape")
x = tuple(y)
print(x)
#Create a new tuple with the value "pineapple", and add that tuple
y = ("pineapple",)
fruit += y
print(fruit)
#Convert the tuple into a list, remove "apple", and convert it back into a tuple
x = ("apple", "orange", "banana")
y = list(x)
y.remove("banana")
x = tuple(y)
print(x)
#remove "banana" from the item using discard() method
thisset = {"apple", "banana", "cherry", "grape"}
thisset.discard("banana")
print(thisset)
#The union() method returns a new set with all items from both sets
x = {"a", "b", "c"}
y = {1, 2, 3}
z = x.union(y)
print(z)
#The union() method returns a new set with all items from both sets
x = {"a", "b", "c"}
y = {1, 2, 3}
x.update(y)
print(x)
#Keep the items that exist in both set x, and set y
x = {"apple", "orange", "cherry", "melon", "banana"}
y = {"cherry", "grape", "apple", "banana", "mango"}
x.intersection_update(y)
print(x)
#Keep the items that are not present in both sets
x = {"apple", "orange", "cherry", "melon", "banana"}
y = {"cherry", "grape", "apple", "banana", "mango"}
z = x.symmetric_difference(y)
print(z)
#Create and print a dictionary
thisdict = {
    "brand": "ford",
    "model": "mustarg",
    "year": 1964
}
print(thisdict)
#Print the "brand" value of the dictionary
thisdict = {
    "brand": "ford",
    "model": "mustarg",
    "year": 1964
}
print(thisdict["brand"])
#Update the "year" of the car by using the update() method
thisdict = {
    "brand": "ford",
    "model": "mustarg",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
    "brand": "ford",
    "model": "mustarg",
    "year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
    "brand": "ford",
    "model": "mustarg",
    "year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change
#rome the "year" of the car by using the pop() method
thisdict = {
    "brand": "ford",
    "model": "mustarg",
    "year": 1964
}
thisdict.pop("year")
print(thisdict)













