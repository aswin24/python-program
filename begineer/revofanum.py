a=input("Enter the values")
b=0
while a>0:
  rm=a%10
  b=b*10+rm
  a=a//10
print "The reverse number is",b
