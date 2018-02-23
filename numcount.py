count = 0
n = input("Enter a Value")
while(int(n) > 0):
    n = int(n) // 10
    count = count + 1
print(count)
