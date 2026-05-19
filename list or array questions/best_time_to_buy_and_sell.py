prices=[7,2,1,5,6,4,8]

def bruteforce(prices):
    profit=0
    max_profit=float("-inf")
    for b in range(0,len(prices)):
        for s in range(b+1,len(prices)):
            profit=prices[s]-prices[b]
            max_profit=max(profit,max_profit)
    return max_profit
print("Brute Force ", bruteforce(prices))


def optimal(prices):
    n=len(prices)
    max_profit=0
    min_price=float("inf")
    for i in range(0,n):
        min_price=min(min_price,prices[i])
        max_profit=max(max_profit,prices[i]-min_price)
    return max_profit

print("Optimal ", optimal(prices))
