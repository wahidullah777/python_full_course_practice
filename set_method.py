a = {1,2,22,3,4,5,6,7,8,}
b={11,22,333,44,55,66,77,88}
print(a)
print(b)

print(a.union(b))
print(a.intersection(b))

a.intersection_update(b) #mean jo value common ho gyi wo show kary gaa 
print(a)

a1 = {1,2,22,3,4,5,6,7,8,}
b1={11,22,333,44,55,66,77,88}
a1.update(b1)
print(a1)

c=a1.symmetric_difference(b1) #mean jo common ni hai value
print(c)