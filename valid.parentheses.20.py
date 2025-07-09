#easy 9jul2025
class Solution:
    def __init__(self):
        self.inStack = []

    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False

        isStrValid = True
        last, curr = None, None

        valid = True
        for _, char in enumerate(s):

            if len(self.inStack) > 0:
                print(self.inStack[-1] + char)
                if (self.inStack[-1] + char) in ['()', '{}', '[]']:
                    print("pop")
                    self.inStack.pop()
                elif (self.inStack[-1] + char) in['{]','{)','[}','[)','(}','(]']:
                    print("stack false")
                    valid = False
                else:
                    print("stack append")
                    self.inStack.append(char)
            else:
                print("stack append")
                self.inStack.append(char)
            
            if not valid:
                break

        if len(self.inStack) != 0:
            print("extras")
            isStrValid = False

        return isStrValid