def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
n=int(input("enter value of a:"))
p=int(input("enter value of b:"))
q=int(input("enter value of c:"))
bignumber=greatest(n,p,q)
print(f"the greatest number among three number is {bignumber}")
