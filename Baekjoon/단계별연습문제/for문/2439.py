N = int(input())
test = '*'
for i in range(N):
    t = f'{test*(i+1)}'
    print(t.rjust(N))