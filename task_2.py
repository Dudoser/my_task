"""
найти общий наибольший делитель двух чисел
"""
a = 18
b = 27
 
while a!=0 and b!=0:
    if a > b:
        a = a % b
    else:
        b = b % a
 
print (a+b)
