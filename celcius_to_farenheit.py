def convert(celsius):
    fahrenheit= (celsius * 9/5)+32
    return fahrenheit
n=int(input("enter the value of temperature in celsius: "))
temp_f = convert(n)
print(f"{n}c is equale to  {temp_f} f ")
