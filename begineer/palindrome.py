a=input("Enter the value:")
b=0
temp=a
while a>0:
  c=a%10
  b=b*10+c
  a=a/10
if temp==b:
  print "It is a Palindrome"
else:
  print "It is not a Palindrome"
