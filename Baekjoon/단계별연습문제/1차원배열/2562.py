import sys

my_list = []
while True:
    for var in sys.stdin.readlines():
        if var == "":
            break
        else:
            my_list.append(map(int, var.strip()))
        
    
print(max(my_list))
print(my_list.max(my_list).index())


