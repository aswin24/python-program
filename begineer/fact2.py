a=input("Enter the values")
f=1
if a>0:
  for i in range(1,a+1):
    f=f*i
  print "The factorial of",a,"is",f
else:
  print "The Factorial of 0 is 1"
