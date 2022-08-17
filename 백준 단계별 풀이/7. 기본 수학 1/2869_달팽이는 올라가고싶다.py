import sys

a, b, v = map(int, sys.stdin.readline().split())

n = v - a
cnt = 1

m = n // (a - b)
cnt += m

k = n % (a - b)
if k > 0:
    cnt += 1

print(cnt)