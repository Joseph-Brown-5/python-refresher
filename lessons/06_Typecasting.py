# Typecasting = the process of converting a variable from one data type to another
#                       str(), int(), float(), bool()

name = "Cups"
age = 31
gpa = 3.8
is_student = True

# you can get the type of a variable using the type() function
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))


# lets convert the gpa to an integer (current float)
gpa = int(gpa)
print(gpa)

# now lets convert age into a float (current integer)
age = float(age)
print(age)

# now lets convert age into a string (current float)
age = str(age)
print(type(age))

# now lets convert name into a boolean (current string)
name = bool(name)
print(name)
print(type(name))
