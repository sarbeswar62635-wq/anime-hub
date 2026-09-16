class solution:
    def concat_array(self,num):
        result  = []
        for i in range(len(num)):
            result.append(num[i])

        for i in range (len(num)):
            result.append(num[i])
        return result
num = list(map(int,input("Enter the elements of array").split()))
obj = solution()
final_result = obj.concat_array(num)
print("concatenation of same array is",final_result)