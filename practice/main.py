
#if statement:
A = 245
B = 300
if A > B:
    print("yes, A is greater then B")
else:
    print("No, A is not greater then B")
#introducing Elif
A = 300
B = 300
if A > B:
    print("yes, A is greater then B")
elif A == B:
    print("A and B are equal")
else:
    print("No, A is not greater then B")
#one line if statement
A = 230
B = 300
if A < B: print("A is less than B")
#one line if else statement
print("A") if A < B else print("B")
#Test if a is less than b, AND if c is greater than a
a = 50
b = 30
c = 45
if a < b and c > a:
    print("both conditions are true")
else:
    print("both conditions are not true")
#Test if a is less than b, AND if c is greater than a
a = 50
b = 30
c = 35
if a < b or c > a:
    print("At least one of the condition is true")
else:
    print("None of the condition is true conditions")
#having if inside if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#Print i as long as i is less than 4
i = 1
while i < 4:
    print(i)
    i += 1
#Print i as long as i is less than 8 Exit the loop when i is 5
i = 1
while i < 8:
    print(i)
    if i == 5:
        break
    i += 1
#Print i as long as i is less than 8 Continue to the next iteration if i is 4
i = 0
while i < 8:
    i += 1
    if i == 4:
        continue
    print(i)
#Print a message once the condition is false
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("i is no lomger less than 5")

#print each fruits in the list
fruits = ["cherry", "mango", "banana", "apple"]
for x in fruits:
    print(x)
#Exit the loop when x is "banana"
fruits = ["cherry", "mango", "banana", "apple"]
for x in fruits:
    if x == "mango":
        break
    print(x)
#Do not print mango
fruits = ["cherry", "mango", "banana", "apple"]
for x in fruits:
    if x == "mango":
        continue
    print(x)
#this increase the sequence by 3
for x in range(2, 30, 3):
    print(x)
#Print all numbers from 0 to 5, and print a message when the loop has ended
for x in range(5):
    print(x)
else:
    print("End of the range sequence")
#Break the loop when x is 3, and see what happens with the else block
for x in range(5):
    if x == 3: break
    print(x)
else:
    print("End of the range sequence") #won't be executed cos of the break introduced
#This function expects 2 arguments, and gets 2 arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("kenneth", "kelvin")
#If the number of arguments is unknown, add a * before the parameter name
def my_function(*footballer):
    print("the best footballer is " + footballer[0])
my_function("saka", "haaland", "mount", "arnold")

