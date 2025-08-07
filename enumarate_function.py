index =0
marks=[12,13,14,15,16,17]
for mark in marks:
   print(mark)
   if(index==3):
      print("wahid is boss  : ")
   index+=1

# enumarate function is ma ye karta hai ky wo index ko bi print karta hia or value ko bi print karta hai to hum ye wala syntax used karty hai 


marks=[12,13,14,15,16,17]

for index, mark in enumerate(marks):
   print(index,mark)
   if(index==3):
      print("wahid is boss  : ")


