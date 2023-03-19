"""
2011번 암호코드: https://www.acmicpc.net/problem/2011
- 알파벳: 총 26글자
- DP
  dp[n] = dp[n-1] + dp[n-2] (11~26번째 알파벳을 만들 수 있는 경우 -> 숫자 2개 합친 경우)
        또는 dp[n-2] (10번, 20번째 알파벳을 만들 수 있는 경우 -> 현재숫자가 0인 경우)
        또는 dp[n-1] (그 외)
- 현재숫자가 0인데 이전숫자가 1, 2가 아니면 해독 불가
"""
num = input().rstrip()

def code(num):
    dp = [0] * len(num)
    dp[0] = 1
    for i in range(1, len(num)):
        if num[i] == '0':
            if num[i-1] == '1' or num[i-1] == '2':
                dp[i] = dp[i-2]
            else:
                return 0
        elif num[i-1] == '1' or (num[i-1] == '2' and num[i] <= '6'):
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
        dp[i] %= 1000000
        
    return dp[-1]

print(code('0' + num))