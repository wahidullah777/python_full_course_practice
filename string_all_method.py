a=" !!  wahidullah  !!!!!"
print(len(a))

print (a.upper()) # captial leter ma convert kar dye ga  
print(a.lower())  # small letter ma convert kar dye gaa

#rstrip method 
print (a)
print(a.rstrip("!")) #rstrip only string ka last waly katam karta hai first waly wahi rhy hai 

# replace method
print(a.replace("wahidullah","ali"))

#split method 
print(a.split(" "))   # split karta hai string ko list ma chnage mtlb string ma jha jha space hpo gyi eha eha ak lis abna dye ga 


#caplitalized method 
a="ulllajaa"
print(a.capitalize( ))   # mtlb first leeter ko capital bana dy gaa


#center method

srg= "this is the boys" 
print(srg.center( 50))  #center ma ly kar ahta hai 

# count method
a= "wahid,ullah,ali,wahid,wahid,ali"
print(a.count("wahid")) #mtlb count karta hai sring kihtne dafa a rhi hai


#endswith method

str1="that is the boys and girls."
print(str1.endswith("girls."))  #mtlb string katam bo gyi hai ky ni true or false ma bta dye ga 

#find  method

str2="he's name is dan. he is the girl"
print(str2.find("is"))     # mtlb find karta ha string ka index number agar koi srring match ni karti to ye -1 return kary ga 

# index method
str3="he's name is dan. he is the girl"
print(str3.index("is"))    #mtlb agar string n mily to ye error dyt ahai  agar mul jye to os index pr ly jta hai


#isalnum method   ( ALPHANUMERIC character) 
s="WelcomeToPakistan4"
print(s.isalnum())  # mean jo string A-Z OR a-z OR 0-9 character say mil kar bani hoi string

#  ISALPHA METHOD (isalphanumeric character )
d ="welcometopk"
print(d.isalpha())  #mean is ma string A-Z OR a-z  string ho gyi

#islower method
f="hello wahid "
print(f.islower()) # islower mean sary caharcter lower case ma ha ky ni 

#isupper method
f="hello wahid "
print(f.isupper()) # isupper mean sary caharcter upper case ma ha ky ni 


#isprintable meethod
h="hello wahid "
print(h.isprintable()) #mean jsy /n printable ni hai ye command used hoti hai next line ma jny ky lye 


#isspace method
j=" "
print(j.isspace()) # mean space ha ky ni 

#istitle method
v="this is the boys "
print(v.istitle())

# startswith meethod
x="python this is the boys "
print(x.startswith("python"))

# swapecase meethod
z="python this is the boys "
print(z.swapcase())

#title method
v="this is the boys "
print(v.title()) # mean first litter ko captial kar dyta hai