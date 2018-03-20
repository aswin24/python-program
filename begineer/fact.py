a=input("Enter the values")
F=1
if a>0:
  for i in range(1,a+1):
    F=F*i
  print "The Factorial of",a,"is",F
else:
  print "The Factorial of 0 is 1"
    
