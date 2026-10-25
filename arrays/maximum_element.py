
def find_maximum(nums):
    if not nums:
        return None

    maximum = nums[0]

    for num in nums:
        if num > maximum:
            maximum = num

    return maximum


# Test cases
print(find_maximum([4, 8, 2, 10, 6]))
print(find_maximum([-5, -2, -10, -1]))
print(find_maximum([7]))
print(find_maximum([]))
