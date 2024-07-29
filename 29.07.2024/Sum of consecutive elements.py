
def max_consecutive_sum(nums, k):
    if not nums or k <= 0:
        return 0
    max_sum = current_sum = sum(nums[:k])
 
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum
a=input().strip()
b=''.join(a)
c=[]
c.append(a)
for nums, k in c:
    result = max_consecutive_sum(nums, k)
    print(f"nums = {nums}, k = {k} => max sum = {result}")
