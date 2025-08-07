r= input("enter the number  : " )
print(f"multipliaction table of {r}")


try: # try mean error ko katam kar dye ga or error ko handle kary gaa 
 for i in range(1,11):
   print(f"{int(r)} X{i} = {int(r)*i}")

except:  # except mean try error ko handle kary ga or jo hum excet kary gye os ko show karwa dya ga 
   
  print("invalid input")
   