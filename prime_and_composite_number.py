n = int(input("Enter the number you want to check"))
if n < 2:
    print("Number is neither prime nor composite")

else:
    count = 0
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            count +=1
    if count > 0:
        print("The number is composite")
    
    else:
        print("Number is not composite ,it is prime")