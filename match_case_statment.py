x=int(input("enter the valueof x:"))
match x:
   case 0:
      print("x is zero")
   case 1:
      print("x is one")
   case _ if x!=80:   # is ma hum if else ka bi used kars akty hai
      print("is not 80")

   case _ if x!=90:
      print("is not 90")
   case _:
      print(x)