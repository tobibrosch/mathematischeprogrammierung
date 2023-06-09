def p(n):
    if n==1: 
        return [1]
    elif n==2: 
        return [1,1]
    else:
        first=[1]
        middle=p(n-1)
        for i in range(len(middle)-1):
            first.append(middle[i]+middle[i+1])
        first= first +[1]
        return first
print(p(11))