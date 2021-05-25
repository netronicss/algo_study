N = int(input())

dp = [0 for _ in range(10 ** 6 + 1)]

dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2

for i in range(5, N + 1):
    ables = [dp[i - 1] + 1]
    if i % 2 == 0:
        ables.append(dp[i // 2] + 1)
    if i % 3 == 0:
        ables.append(dp[i // 3] + 1)

    dp[i] = min(ables)

print(dp[N])