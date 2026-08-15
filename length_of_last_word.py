class Solution:
    def lengthOfLastWord(self, s):
        words = s.split()
        return len(words[-1])
s = input("Enter a sentence: ")

obj = Solution()
result = obj.lengthOfLastWord(s)

print("Length of last word:", result)