import sys

def main():
    data = sys.stdin.read().split()
    S, D, G = int(data[0]), int(data[1]), int(data[2])
    s1 = data[3]
    s2 = data[4]

    n, m = len(s1), len(s2)

    # Smith-Waterman local alignment
    # dp[i][j] = best score of alignment ending at s1[i-1] and s2[j-1]
    # Transitions:
    #   match/mismatch: dp[i-1][j-1] + S or -D
    #   gap in s2 (skip s1[i-1]): dp[i-1][j] - G
    #   gap in s1 (skip s2[j-1]): dp[i][j-1] - G
    # Floor at 0 handles the "choose any substring" part

    prev = [0] * (m + 1)
    ans = 0

    for i in range(1, n + 1):
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            score = S if s1[i - 1] == s2[j - 1] else -D
            val = max(
                0,
                prev[j - 1] + score,  # match or mismatch
                prev[j] - G,           # gap: skip s1[i-1]
                curr[j - 1] - G        # gap: skip s2[j-1]
            )
            curr[j] = val
            if val > ans:
                ans = val
        prev = curr

    print(ans)

main()