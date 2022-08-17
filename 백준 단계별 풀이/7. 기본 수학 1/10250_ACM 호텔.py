import sys

test_n = int(sys.stdin.readline())

for _ in range(test_n):
    h, w, n = map(int, sys.stdin.readline().split())

    if n % h <= 0:
        height = str(h)
    else:
        height = str(n % h)
    
    if n % h != 0:
        number = str(n // h + 1)
    else:
        number = str(n // h)

    if int(number) < 10:
        string = height + "0" + number
    else:
        string = height + number

    print(string)