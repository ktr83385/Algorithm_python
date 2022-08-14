import sys

n = int(sys.stdin.readline())

i = 6
count = 0
temp = 1

while True:
    temp = temp + i * count
    if n <= temp:
        print(count + 1)
        break
    
    count += 1