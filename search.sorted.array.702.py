class ArrayReader:
   def get(self, index: int) -> int:
    pass

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        found = False
        prevIndex, index, n, exceeded = 0, 0, 0, False
        
        while found is False:
            secret = reader.get(index)
            if secret < target:
                print("less", secret)
                if not exceeded:
                    prevIndex = index
                    n+=1
                    index = 2**n
                else:
                    temp = index
                    step = (index - prevIndex) //2
                    if step < 1: 
                        break 
                    index += step
                    prevIndex = temp
            elif secret > target:
                print("more", secret)
                exceeded = True
                print("exceeded!")
                step = (index - prevIndex)//2 
                if step < 1: 
                    break 
                index = prevIndex + step
            else:
                found = True
                break
        if not found: 
            return -1
        return index
    
'''
RE-ATTEMPT
THis was not done in a straight one attempt 
This needs to be studied for smoother attempt
'''