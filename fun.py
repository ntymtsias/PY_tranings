class Solution():
    def minDis(self, word1: str, word2: str)-> int:
        n = len(word1)
        m = len(word2)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    print('+1')
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i][j-1])+1
        return dp[n][m]

        print()


cl = Solution()
x = cl.minDis("Nazar", "lol")
print(x[5][4])


#print all

for i in range(len(x)):
    for j in range(len(x[0])):
        print(x[i][j],end=' ')
    print()
