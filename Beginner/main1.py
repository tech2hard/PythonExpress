x = "great"

def myfunc():
  print("Python is " + x)

def myTest1():
    print(x + "is Python")

def funHelloWorld():
    print("Hello World python")

myfunc()
myTest1()
funHelloWorld()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


def myfunc():
  global x
  x = "global term fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "perm fantastic"

myfunc()

print("Python is " + x)


#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

#print by converting type
x = 5
print(type(x))

