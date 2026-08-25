class majority():
    def element(self,n):
        count = {}
        for i in n:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            if count[i]>len(n)/2:
                return i
n = list(map(int,input("Enter numbers").split()))
obj = majority()
result = obj.element(n)
print(result)