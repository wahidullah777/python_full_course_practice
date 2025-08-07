def foctorial(n):
    if(n==0) or (n==1):
        return 1
    else:
       return n * foctorial(n-1) 
print (foctorial(5))
print (foctorial(4))# function call
print (foctorial(3))
print (foctorial(2))
print (foctorial(1)) 