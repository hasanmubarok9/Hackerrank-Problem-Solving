def arrayManipulation(n, queries):
    list = [0]*(n+1)
    print('list ', list)
    for _ in queries:
        x, y, incr = _
        print('x ', x)
        print('y ', y)
        print('incr ', incr)
        list[x-1] += incr
        if((y) <= len(list)):
            list[y] -= incr
        print('list ', list)
    max = x = 0
    for i in list:
        x = x+i
        if(max < x):
            max = x
        print('x ', x)
        print('max ', max)
    return max


print(arrayManipulation(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]))
