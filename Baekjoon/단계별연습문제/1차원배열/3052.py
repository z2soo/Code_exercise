result = []

for i in range(10):
    var1 =  int(input())
    var2 = var1 % 42
    if var2 in result:
        pass
    else:
        result.append(var2)
        
print(len(result))


        
