n = int(input("Enter the number"))
s = 0
for i in range(1,n):
    if n % i == 0:
        s +=1
if s == n:
    print("The number is perfect")
else:
    print("Number is not perfect") 