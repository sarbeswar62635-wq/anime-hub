class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        a = 1
        b = 2
        for i in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return b

n = int(input("Enter number of stairs: "))
obj = Solution()
result = obj.climbStairs(n)
print(f"The number of ways to climb stairs is {result}")