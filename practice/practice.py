#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name
# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#With list comprehension you can do the above with just a line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x ]
print(newlist)

#write a command line that only accept items that are not banana
newlist = [x for x in fruits if x != "banana"]
print(newlist)

#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

#write a command line that only accept nymbers less than 6
newlist = [x for x in range(10) if x < 6]
print(newlist)

#sort the list alphabetically
fruits = ["orange", "mango", "apple", "pineapple", "banana"]
fruits.sort()
print(fruits)

#sort the list descending
fruits = ["orange", "mango", "apple", "pineapple", "banana"]
fruits.sort(reverse=True)
print(fruits)

#reverse the order of the list items

fruits = ["orange", "mango", "apple", "pineapple", "banana"]
fruits.reverse()
print(fruits)

#join the 2 list
list1 = ('a', 'b', 'c')
list2 = (1, 2, 3)
list3 = list1 + list2
print(list3)

#you can use Append join lists
list1 = ('a', 'b', 'c')
list2 = (1, 2, 3)
for x in list2:
    list1.append(x)

print(list1)
