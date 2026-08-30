class solution:
    def intersection(self,num1,num2):
        set1 = set(num1)
        set2 = set(num2)
        return list(set1 & set2)

num1 = list(map(int,input("enter the numbers of first list").split()))
num2 = list(map(int,input("enter the numbers of second list").split()))
obj = solution()
result = obj.intersection(num1,num2)

print(result)