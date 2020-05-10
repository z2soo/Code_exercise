# 양수양수 1
# 음수 양수 2
# 음수 음수 3
# 양수 음수 4

x = int(input())
y = int(input())

if x*y > 0:
    if x > 0:
        print(int(1))
    else:
        print(int(3))
else:
    if x > 0:
        print(int(4))
    else:
        print(int(2))