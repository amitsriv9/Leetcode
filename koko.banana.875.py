from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        totalBananas = 0
        maxPile = 0
        returnMaxPile = False
        
        if h == len(piles):
            returnMaxPile = True
        extraTime = h - len(piles)

        for index, pile in enumerate(piles):
            totalBananas += pile
            if maxPile < pile:
                maxPile = pile

        if returnMaxPile:
            return maxPile

        avgBanana = totalBananas // h 
        remainingPiles = 0
        remainingBananas = 0
        
        while True: 
            for index, pile in enumerate(piles):
                if pile - avgBanana > 0:
                    remainingPiles += 1
                    remainingBananas += (pile - avgBanana)
        
            if remainingPiles > extraTime:
                avgBanana += 2
                continue
            else:
                break
        
        if remainingBananas <= avgBanana*extraTime:
            return avgBanana
        else:
            return avgBanana
        
    '''
    once you know the avgBananas per hour 
    determine extra time we have, say N
    find the Nth largest value and determine remainder 

    example 
    1,3,5,7,9,14  total 39 H=7 k=9 delta = 1  avg 6
    thus we choose 2nd largest value ie 9 
    then check if 11 can be consumed in 2 9s

    1,3,5,7,9,21  total 47 H=7 delta = 1 
    ''' 

    def solution(self, piles: List[int], h:int) -> int:
        maxPile = 0
        totalBananas = 0
        for index, pile in enumerate(piles):
            totalBananas += pile
            if maxPile < pile:
                maxPile = pile

        if len(piles) == h:
            return maxPile

        # least bananas per hour 
        avgBananas = totalBananas // h
        
        if totalBananas % h != 0:
            avgBananas += 1
        print("Avg Bananas:", avgBananas)

        remainingPiles, remainingBananas = 0, 0
        remainingList = []

        for index, pile in enumerate(piles):
            if pile - avgBananas > 0:
                remainingPiles += 1
                remainingBananas += pile - avgBananas
                remainingList.append(pile-avgBananas)

        remainingHours = h - len(piles)
        print("remainingHours: ", remainingHours, "remainingPiles: ", remainingPiles)
        if remainingHours < remainingPiles:
            temp = remainingPiles - remainingHours            
            remainingList.sort()
            avgBananas += remainingList[-temp]
            print("Case1:Avg Bananas:", avgBananas)
        
        else:
            hoursNedeed = remainingBananas // avgBananas
            print("needed", hoursNedeed, " remaining ",remainingHours)
            while hoursNedeed > remainingHours:    
                avgBananas += 1
                remainingBananas -= len(pile)
                hoursNedeed = remainingBananas // avgBananas
            print("Case2:Avg Bananas:", avgBananas)
        
        return avgBananas