class subarray():
    def max_subarray(self,nums):
        current = nums[0]
        maximum = nums[0]
        for i in range(1,len(nums)):
            current = max(nums[i],current + nums[i])
            maximum = max(maximum , current)
        return maximum
nums = list(map(int,input("Enter numbers:").split()))
obj = subarray()
result = obj.max_subarray(nums)
print("maximu sumof subarray is:",result)