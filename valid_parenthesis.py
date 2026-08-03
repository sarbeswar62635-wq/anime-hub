class parenthesis:
    def isvalid(self,s:str)-> bool:
        stack = []
        pairs = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for ch in s:
            print("charecter:",ch)
            print("stack:",stack)
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
        return len(stack)==0
s = input("enter the brackets you want check if valid or not")
valid = parenthesis()
print(valid.isvalid(s))
