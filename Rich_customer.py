class solution:
    def max_wealth(self,accounts):
        richest = 0

        for row in accounts:
            wealth = sum(row)
            if wealth > richest:
                richest = wealth
        return richest

accounts = []
A =int(input("Enter number of customer"))
B =int(input("Enter number of bank"))
for i in range(A):
    row = list(map(int,input("Enter amounts").split()))
    accounts.append(row)
obj = solution()
result = obj.max_wealth(accounts)
print(result)
