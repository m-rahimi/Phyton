"""Given an array of numbers representing the stock prices of a company in chronological order and an integer k, 
return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, 
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1] you should return 3."""

def maximize_profile(prices, K):
    N = len(prices)
    dp = [[None]*(N+1) for i in range(K+1)]  # None means no profit.
    dp[0] = [0] * (N+1) # 0 buys and sells (base case)
    for k in range(1, K+1):  # k buys and selss
        for i in range(1, N+1): # first i elements and sell at i-1th index
            for j in range(i-1): # buy at jth index. I can't buy and sell at the same index
                if dp[k-1][j] is not None:
                    if dp[k][i] is None:
                        dp[k][i] = dp[k-1][j] + prices[i-1] - prices[j]
                    else:
                        dp[k][i] = max(dp[k][i], dp[k-1][j] + prices[i-1] - prices[j])
    
    print(dp)
    result = 0
    for i in range(1, N+1):
        if dp[K][i] is not None:
            result = max(result, dp[K][i])
    return result
