from typing import List
# revisit for improvement in efficiency
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, max_profit = -1,0
        calc_profit = True
        for index, price in enumerate(prices):
            print(price)
            if buy_price == -1:
                buy_price = price
            elif buy_price > price:
                buy_price = price
                calc_profit = True
            else:
                if calc_profit:
                    print(f"the buy price is {buy_price}")
                    profit, sell_price = self.max_sell_price(buy_price, prices[index:])
                    calc_profit = False
                    if max_profit < profit:
                        max_profit = profit
        print(max_profit)
        return max_profit

    def max_sell_price(self, buy_price, price_list):
        max_profit, max_price = 0,0
        for _, price in enumerate(price_list):
            if price > buy_price:
                profit = price - buy_price
                if max_profit < profit:
                    max_profit  = profit
                    max_price = price
        return max_profit, max_price
    

import unittest
class Tests(unittest.TestCase):
    def testcase1(self):
        obj = Solution()
        profit = obj.maxProfit([6,5,4,3,2,1])
        self.assertEqual(profit, 0)

    def testcase2(self):
        obj = Solution()
        profit = obj.maxProfit([5,2,3,4,5,6,7])
        self.assertEqual(profit, 5)

    def testcase3(self):
        obj = Solution()
        profit = obj.maxProfit([2,1,2,1,0,1,2])
        self.assertEqual(profit, 2)

if __name__=='__main__':
    unittest.main()


'''
for a given buy price
scan the array determine the max sale price for the buying price

in next iteration of the new buy price is higher skip, if lower adjust the profit

'''