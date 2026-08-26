class solution:
    def plus_one(self,n):
        for i in range(len(n)-1,-1,-1):
            if n [i] < 9:
                n [i]+=1
                return n
            else:
                n [i]=0

n = list(map(int,input("Enter the numbers").split()))
obj = solution()
result = obj.plus_one(n)
print(result)
