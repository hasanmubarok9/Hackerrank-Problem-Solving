def hourglassSum(arr):
    hourglass = []
    for i in range(4):
        for j in range(4):
            vallen = []
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if (k == (i + 1)) and ((l == j) or l == (j + 2)):
                        continue
                    vallen.append(arr[k][l])
            hourglass.append(sum(vallen))
    return max(hourglass)

# test case 0

# print(len(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [
#     0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]])))
# for item in hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [
#         0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]):
#     print(len(item))
#     print(item)

# test case 1


print(hourglassSum([[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9,
                                                                 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]))
