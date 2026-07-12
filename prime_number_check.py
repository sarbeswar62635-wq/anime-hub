def primenumber(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num = int(input( " enter your number "))
print(primenumber(num))