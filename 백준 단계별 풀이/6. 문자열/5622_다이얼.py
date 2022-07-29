import sys

alphabet_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
req_time_list = [3, 4, 5, 6, 7, 8, 9, 10]

string = sys.stdin.readline().strip()

time = 0

for i in range(len(string)):
    for idx, j in enumerate(alphabet_list):
        if string[i] in j: 
            time += req_time_list[idx]

print(time)