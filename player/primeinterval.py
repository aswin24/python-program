a=int(input("Enter the value"))
b=int(input("Enter the value"))
print "prime numbers between ",a,"and",b,"is"
for n in range(a,b+1):
  if n >1:
    for i in range(2,n):
      if(n %i ==0):
        break
    else:
      print n
