n = int(input("Enter the number "))
temp = n
digits = len(str(n))
s = 0
while temp > 0:
    digit = temp % 10
    s+= digit**digits
    temp//=10
if s==n:
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")