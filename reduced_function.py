from functools import reduce
list1=[1,2,3,4,5]
def sum(a,b):
   return a+b
wahid =reduce(sum,list1)
print(wahid)
