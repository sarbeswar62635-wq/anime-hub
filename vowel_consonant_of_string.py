n=input(" enter a string ")
vowles = 0
consonant=0
for ch in n:
    if ch in "aeiouAEIOU":
        vowles +=1
    elif ch.isalpha():
        consonant+=1
print(" number of vowles is " , vowles)                    
print(" number of  is consonant " , consonant)