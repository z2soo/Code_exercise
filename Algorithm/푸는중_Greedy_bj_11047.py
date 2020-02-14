N, K = map(int, input().split( ))
coin = sorted([int(input()) for i in range(N)], reverse=True)


while k % p !=0:
    for p in coin:
        rest = K % p

print(coin)