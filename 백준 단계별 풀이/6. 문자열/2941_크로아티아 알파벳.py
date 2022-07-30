import sys

string = sys.stdin.readline().strip()

count = len(string)

croatia_alphbet_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_alphbet_list:
    if i in string:
        count -= string.count(i) * (len(i) - 1)
        string = string.replace(i, ' ')

print(count)