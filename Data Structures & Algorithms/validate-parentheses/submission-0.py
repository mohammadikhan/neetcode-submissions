class Solution:
    def isValid(self, s: str) -> bool:

        hashMap = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for bracket in s:
            if bracket in hashMap:
                if stack and stack[-1] == hashMap[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return True if not stack else False
            
            
        