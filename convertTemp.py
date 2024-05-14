
#pivot index is 3 -- 6 
#left 1+7+3
#right 6+5

#first let's create the presum array
# then if pointer is 0 the left become 0 and pointer is len(arr)-1 right becomes 0
nums = [1]

n = len(nums)
pxsum = [nums[0]]
for i in range(1,n):
    pxsum.append(nums[i]+pxsum[i-1])

for j in range(n):
    if j == 0:
        left = 0
        right = pxsum[n-1]-pxsum[j]
    elif j == n-1:
        right = 0
        left = pxsum[j-1]
    else:
        left = pxsum[j-1]
        right = pxsum[n-1]-pxsum[j]
    if left == right:
        print(j)
