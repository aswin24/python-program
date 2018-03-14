a=input("Enter the Value")
sum=0
g=len(str(a))
nem=a
for i in range(0,a):
  r=a%10
  sum=sum+(r**g)
  a=a//10
if sum==nem:
  print "Armstrong number"
else:
  print "not a Armstrong number"
