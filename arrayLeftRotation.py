# first solution
array = [1, 2, 3, 4, 5]

# # shift 3 index
# for i in range(3):
#     array.append(array.pop(0))

# print(array)

# second solution

d = 11

d = d % len(array)

print(d)

array = array[-d:] + array[:-d]

print(array)
