num = int(input()) 
floor =list(map(int, input().split( )))
result = 0

'''for i in range(num):
    k = int(input())
    buildings.append(k)
'''
for t in range(num):
    if floor[t] == 0:
        pass

    elif floor[t] != 0:
        to_check = [floor[t-2],floor[t-1],floor[t+1],floor[t+2]]
        be_check = [floor[t] for i in range (4)]
        mylist = []

        for p in range(4):
            mylist.append(be_check[p]-to_check[p])
            
        if mylist > [0,0,0,0] == True:
            print(mylist)
            result = result + min(mylist)
            print(result)
