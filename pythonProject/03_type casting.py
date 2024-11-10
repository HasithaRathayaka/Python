name ="Hasitha"
age = 22
gpa = 1.9
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

#typecasting converting a value of one data type into another data type
        #Explicit type casting maually doing
age = float(age)
print(age)
print(type(age))

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = bool(age)
print(age)

        #Implicit type casting convert datatype automatically
x = 2
y = 2.0

x = x/y
print(x)