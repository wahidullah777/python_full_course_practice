# lecture no 48   local or global variable 
x=9   #global variable 
print(x)
def loccaly():
    global x # kis behir waly ko golbal banny ky lye global keyword use kia jta or or agye varaible ka name ahta ha
x=10
     
y=6  # local variable 
print(y)
   
print(x)

loccaly() # function call


print(y)