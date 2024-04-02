#Identity Operator
a=67
b=56
c=56
print(a is not b)
print(a is c)
print(b is c)
print(b is not c)
print(id(b))
print(id(c))
x=[1,2,3,4,5]
y=[1,2,3,4,5]
print(x is y) #different location
print(id(x))
print(id(y))