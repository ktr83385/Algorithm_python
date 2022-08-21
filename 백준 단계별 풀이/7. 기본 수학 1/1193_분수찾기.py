import sys

n = int(sys.stdin.readline())

x, y = 1, 1
count = 1
flag = 0

if n == 1:
    st = str(x) + "/" + str(y)
    print(st)
else:
    while True:
        if x == 1:
            if count == n:
                st = str(x) + "/" + str(y)
                print(st)
                flag = 1
                break

            y += 1
            count += 1
            
            for _ in range(y - 1, 0, -1):
                if count == n:
                    st = str(x) + "/" + str(y)
                    print(st)
                    flag = 1
                    break
                x += 1
                y -= 1 
                count += 1

        elif y == 1:
            if count == n:
                st = str(x) + "/" + str(y)
                print(st)
                flag = 1
                break

            x += 1
            count += 1

            for _ in range(x - 1, 0, -1):
                if count == n:
                    st = str(x) + "/" + str(y)
                    print(st)
                    flag = 1
                    break
                    
                x -= 1
                y += 1
                count += 1

        if flag == 1:
            break