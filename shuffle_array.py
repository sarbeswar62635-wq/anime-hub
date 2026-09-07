class solution:
    def shuffel_array(self,nums):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result

n = int(input("Enter the number of element in each half"))
nums = list(map(int,input("Enter the list").split()))
obj = solution()

solution_problem = obj.shuffel_array(nums)
print(solution_problem)