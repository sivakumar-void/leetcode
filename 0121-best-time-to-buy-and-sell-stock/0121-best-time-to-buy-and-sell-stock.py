class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==sorted(prices,reverse=True) or len(prices)==1 or len(prices)==0:
            return 0
        else:
            buy=0
            sell=1
            profits=[]
            while sell<=len(prices)-1:
                if prices[buy]<prices[sell]:
                    profits.append(prices[sell]-prices[buy])
                    
                
                else:
                    buy=sell
                sell+=1
            return max(profits) if len(profits)>0 else 0


        
        
        
            
        