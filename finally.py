def fun1():
 try:
  a=[3,4,5,6,7]
  n=int(input("enter the number :"))

  print(a[n])
  return 1
 except:
  print("this is not interger value ")
  return 0
 finally:
  print("i am always executed ")

x= fun1()
print(x)