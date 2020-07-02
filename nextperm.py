# 
# Next lexicographical permutation algorithm (Python)
# by Project Nayuki, 2014. Public domain.
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# 


# -- Basic version --
# 
# Computes the next lexicographical permutation of the specified list in place,
# returning whether a next permutation existed. (Returns False when the argument
# is already the last possible permutation.)
# 
def biggerIsGreater(w):
	# w = list(w)
	print("w : ", w)
	# Find non-increasing suffix
	i = len(w) - 1
	while i > 0 and w[i - 1] >= w[i]:
		i -= 1
	
	print("i : ", i)
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(w) - 1
	while w[j] <= w[i - 1]:
		j -= 1

	print("j : ", j)
	w[i - 1], w[j] = w[j], w[i - 1]
	
	print("w : ", w)
	
	# Reverse suffix
	w[i : ] = w[len(w) - 1 : i - 1 : -1]
	return w

# Example:
#   arr = [0, 1, 0]
#   next_permutation(arr)  (returns True)
#   arr has been modified to be [1, 0, 0]


# -- Comparator version --
# 
# Computes the next lexicographical permutation of the specified list in place,
# returning whether a next permutation existed. (Returns False when the argument
# is already the last possible permutation.)
# 
# comp is a comparison function - comp(x, y) returns a negative number if x is considered to be less than y,
# a positive number if x is considered to be greater than y, or 0 if x is considered to be equal to y.
# 
def next_permutation_comp(arr, comp):
	# Find non-increasing suffix
	i = len(arr) - 1
	while i > 0 and comp(arr[i - 1], arr[i]) >= 0:
		i -= 1
	if i <= 0:
		return False
	
	# Find successor to pivot
	j = len(arr) - 1
	while comp(arr[j], arr[i - 1]) <= 0:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Reverse suffix
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True

# print(biggerIsGreater("hasan"))
# print(biggerIsGreater([0, 1, 7, 5, 3, 2, 3]))
print(biggerIsGreater([0, 1, 7, 5, 3, 2, 0]))