class solution:
    def isAnagram(self,s,t):
        return sorted(s) == sorted(t)
s = input("enter the string ")
t = input("enter another string ")
Valid = solution()
print(Valid.isAnagram(s,t))