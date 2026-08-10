class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)
nums = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter target: "))

obj = Solution()
result = obj.searchInsert(nums, target)

print("Insert position (index):", result)
