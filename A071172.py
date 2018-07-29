// http://oeis.org/A071172
// 有更快的方法.详细见 PE193
from math import sqrt
from math import floor
import time
def mobius_sieve(lim):
    m = floor(sqrt(lim))
    mu = [1] * (lim + 1)
    for i in range(2, m + 1):
        if mu[i] == 1:
            for j in range(i, lim+1, i):
                mu[j] *= -i
            for j in range(i*i, lim+1, i*i):
                mu[j] = 0
    for i in range(2, lim+1):
        if mu[i] == i:
            mu[i] = 1
        elif mu[i] == -i:
            mu[i] = -1
        elif mu[i] < 0:
            mu[i] = 1
        elif mu[i] > 0:
            mu[i] = -1
    return mu

# return the number of squarefree integers <n.
memo = {}
def counting_sqaurefree_numbers(n):
    try:
        return memo[n]
    except KeyError:
        limit = floor(sqrt(n) + 1)
        mob = mobius_sieve(limit)
        ans = 0
        for k in range(1, limit):
            ans += mob[k] * (n // (k ** 2))
        memo[n] = ans
        # print("sqaurefree_num = %d " % ans)
        print(ans)

if __name__ == "__main__":
    # s = time.perf_counter()
    counting_sqaurefree_numbers(10**6)
    counting_sqaurefree_numbers(10**8)
    counting_sqaurefree_numbers(10**15)
    # e = time.perf_counter()
    # print(e - s)

