class solution:
    def contain_duplicate(self,nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
nums = list(map(int,input("Enter numbers:").split()))
obj = solution()
result = obj.contain_duplicate(nums)
print("Is the aray contain duplicate?",result)