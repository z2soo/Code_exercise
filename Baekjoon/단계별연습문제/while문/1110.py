# 10보다 작으면 0을 붙여 두글자로 만들기
# 두 글자를 더하기
# 기존 글자 오른쪽, 합 글자의 오른쪽 붙여서 새로운 수 

mylist = list(map(int, input()))


def myfunc(mylist):
    first = mylist
    cnt = 1
    while True:
        result = []
        if len(mylist) < 2:
            mylist.insert(0,0)
        else:
            result.append(mylist[1])
            sum_list = list(str(sum(mylist)))
            result.append(int(sum_list[-1]))
            if first == result:
                return cnt
                break
            else:
                mylist = result
                cnt = cnt+1

print(myfunc(mylist))
