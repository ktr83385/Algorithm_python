import sys

n = int(sys.stdin.readline())

cnt_5 = n // 5
modified_n = n % 5

if modified_n == 0:
    print(cnt_5)
else:
    cnt_3 = 0
    cnt_remains = 0

    while True:

        if modified_n % 3 != 0:
            if cnt_5 > 0:
                cnt_5 -= 1
                modified_n += 5

            elif cnt_5 == 0 and modified_n % 3 != 0:
                print(-1)
                break

        elif modified_n % 3 == 0:
            cnt_3 = modified_n // 3
            print(cnt_5 + cnt_3)
            break