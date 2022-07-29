import sys

a, b = sys.stdin.readline().split()

string_a = ""
string_b = ""

for i in range(len(a) - 1, -1, -1):
    string_a += a[i]

for i in range(len(b) - 1, -1, -1):
    string_b += b[i]

int_a = int(string_a)
int_b = int(string_b)

if int_a < int_b:
    print(string_b)
else:
    print(string_a)