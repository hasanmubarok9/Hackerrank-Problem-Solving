def longestSubarray(arr):
    # Write your code here
    subArr = [] 
      
    # first loop  
    for i in range(len(arr) + 1): 
          
        # second loop  
        for j in range(i + 1, len(arr) + 1): 
              
            # slice the subarray  
            sub = arr[i:j] 
            if sub not in subArr and len(set(sub)) <= 2 and (max(sub)-min(sub) <= 1):
                subArr.append(sub) 
              
      
    return max(subArr, key=len)


print(longestSubarray([0, 1, 2, 1, 2, 3]))
print(longestSubarray([1, 1, 1, 3, 3, 2, 2]))
print(longestSubarray([1, 2, 3, 4, 5]))
print(longestSubarray([2, 2, 1]))