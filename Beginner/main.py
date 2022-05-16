##Print Statement
print("Hello, World!")
##exit()

##This is how comments are written

## if else statements
if 5 > 2:
  print("Five is greater than two!")
else:
    print ("Else loop")

## Python Variables
x=5
y="Hardi"

print(x)
print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

print(type(x))
print(type(y))

x = "Hardi"
# is the same as
x = 'Joshi'
print(type(x))

#Legal Variable names
testvar = "Joshi"
test_var = "Joshi1"
_test_var = "Joshi2"
testVar = "Joshi3"
TESTVAR = "Joshi4"
testvar2 = "Joshi5"

##illegagl Variable Names

#2myvar = "John"
#my-var = "John"
#my var = "John"

#Camel Case
myVariableName = "Hardi"
print(myVariableName)
#Pascal Case
MyVariableName = "Joshi"
print(MyVariableName)
#Snake Case
my_variable_name = "Josh"
print(my_variable_name)

###Variable Assignment 
x, y, z = "1-Orange", "2-Banana", "3-Cherry"
print(x)
print(y)
print(z)

###One Value to Multiple Variables
x = y = z = "Kiwi"
print(x)
print(y)
print(z)

##Unpack a Collection
fruits = ["apple1", "banana2", "cherry3"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z, "there")

x = "Python "
y = "is "
z = "awesome"
print(x + y + z+ " Here")

x = 5
y = "John"
##print(x + y) --Code will throw error

## Print variable with 2 diff datatype
x = 5
y = "John"
print(x, y)