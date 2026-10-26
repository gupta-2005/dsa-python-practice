
def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# Test cases
print(max_subarray([-2, 1, -3, 4, -1, 2, 1]))
print(max_subarray([5, 4, -1, 7, 8]))
print(max_subarray([-3, -2, -5]))
print(max_subarray([1]))
