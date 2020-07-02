def minimumSwap(arr):
    n = len(arr)

    enumeratedArr = [*enumerate(arr)]

    print('enumeratedArr before sort ', enumeratedArr)

    enumeratedArr.sort(key=lambda gelas: gelas[1])

    visited = {i: False for i in range(n)}

    print('enumeratedArr ', enumeratedArr)

    ans = 0
    for i in range(n):

        if visited[i] or enumeratedArr[i][0] == i:
            continue

        cycle = 0
        j = i
        while not visited[j]:

            print('j ', j)
            print('enumeratedArr[j][0] ', enumeratedArr[j][0])

            visited[j] = True

            j = enumeratedArr[j][0]

            cycle += 1

        if cycle > 0:
            ans += (cycle - 1)

    return ans


# print(minimumSwap([2, 4, 5, 1, 3]))
# print(minimumSwap([4, 3, 2, 1]))
# print(minimumSwap([2, 1, 5, 3, 4]))
print(minimumSwap([2, 5, 1, 3, 4]))
