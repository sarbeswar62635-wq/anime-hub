class number:
    def appear_number(self,n):
        result = 0
        for i in n:
            result = result ^ i
        return result

n = list(map(int, input("Enter numbers:").split()))
obj = number()
sol = obj.appear_number(n)
print(f"The single appear number in given string is{sol}")