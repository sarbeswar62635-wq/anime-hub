class solution:
    def pivot_index(self,n):
        total = sum(n)
        left = 0
        for i in range(len(n)):
            right = total - left -n[i]
            if left==right:
                return i
            left +=n[i]
        return -1
n = list(map(int,input("Enter the numbers").split()))
obj = solution()
result = obj.pivot_index(n)
print(result)