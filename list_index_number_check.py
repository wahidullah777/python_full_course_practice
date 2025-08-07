name=["wahid",7,8,9,100, 9.8,"ali","ahamd","hassan"]
print(name)

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print(name[-3])
print(name[len(name)-3])# mean ap total ma sy is ko - kar do baki value + ma a jye gyi to kaam asan ho jye ga 
print(name[5-3]) #postive index numbetr

# ye check kia ka ali is list m aha ky ni agar ha to yes agar ni ha to no dye 
if "ali" in name:
 print("yes")
else:
 print("no")

 print(name[1:8:3])