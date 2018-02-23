n = input("Enter the year")
if n % 4 == 0 and n % 100!=0 or n % 400 == 0:
    print('The year', n,'is a leap year')
else:
    print('The year', n,'is not a leap year')
