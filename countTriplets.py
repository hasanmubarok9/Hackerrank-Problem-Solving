from collections import defaultdict
def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        print("nilai k ", k)
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1
        print("nilai count ", count)
        print("nilai v3 ", v3)
        print("nilai v2 ", v2)

    return count

# print(countTriplets([1 for _ in range(100)], 1))
print(countTriplets([1, 3, 9, 9, 27, 81], 3))
# print(countTriplets([1, 5, 5, 25, 125], 5))