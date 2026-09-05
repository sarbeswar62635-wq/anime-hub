class solution:
    def running_array(self,num):
        total = 0
        result = []
        for i in range(len(num)):
            total += num[i]
            result.append(total)
        return result
        
num = list(map (int,input("Enter the array").split()))
obj = solution()
sum_of_running_array = obj.running_array(num)
print(sum_of_running_array)