
#Problem 1: Object Types (Weight 2). Consider the number 17. Construct multiple variables (y1, y2, y3,
#and y4) in Python that represent the number 17 in the various forms of objects (integer, float, string,
#and Boolean, respectively). Hint: For creation of the Boolean, set a value for 17 to be compared against
#another number.

#Print the value of y1, y2, y3, and y4 and their types (Hint: you can use function type() to
#get a type of an object or variable).

y1 = int(17)
print(y1)
print(type(y1))

y2 = float(17)
print(y2)
print(type(y2))

y3 = "17"
print(y3)
print(type(y3))

y4 = bool(17==4)
print(y4)
print(type(y4))

#Use y1, y2, or y3 to create a variable named text such that print(text) prints 'The
#value of x is 17.'

text = "The value of x is "+str(y1)+"."
print(text)

