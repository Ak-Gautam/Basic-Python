'''
Mural Problem
Thanh wants to paint a wonderful mural on a wall that is N sections long. Each section of the wall has a beauty score, which indicates how beautiful it will look
if it is painted. Unfortunately, the wall is starting to crumble due to a recent flood, so he will need to work fast!
At the beginning of each day, Thanh will paint one of the sections of the wall. On the first day, he is free to paint any section he likes. On each subsequent day,
he must paint a new section that is next to a section he has already painted, since he does not want to split up the mural.
At the end of each day, one section of the wall will be destroyed. It is always a section of wall that is adjacent to only one other section and is unpainted
(Thanh is using a waterproof paint, so painted sections can't be destroyed).
The total beauty of Thanh's mural will be equal to the sum of the beauty scores of the sections he has painted. Thanh would like to guarantee that,
no matter how the wall is destroyed, he can still achieve a total beauty of at least B. What's the maximum value of B for which he can make this guarantee?
'''




def solve(n, a):
    print("Input:", n, a)
    b = [0] * (a + 1)
    for i in range(1, n + 1):
        b[i] = b[i - 1] + a[i - 1]
    res = 0
    half = (n + 1) // 2
    for i in range(n):
        if i + half <= n:
            res = max(res, b[i + half] - b[i])
    return res


def main():

    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        a = map(int, input().strip())
        a = list(a)
        res = solve(n, a)
        out = "Case #%d: %s\n" % (i + 1, res)
        print(out)


main()
