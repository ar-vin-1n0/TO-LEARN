nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



def q1(nums):
     nums_rev = nums[::-1]
     return nums_rev

def q2(nums):
    unique_nums = set(nums)
    unique_nums.sort()
    return unique_nums[-2]

def q3(nums):
    seen = set()
    cleaned = []
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            cleaned.append(num)

    return cleaned

def q4(nums,k):
    k = k % len(nums)

    rotated = nums[-2:] + nums[:-2]

    return rotated

def q5(nums):
    num_of_nums = len(nums)
    return num_of_nums

def q6(nums):
    nums2 = [11,12,13,14,15,16,17,18,19,20]
    merged_list = nums + nums2
    return merged_list.sort()

def q7(value:str):
    if value == value[::-1]:
        return True
    else:
        return False

def q8(nums:list):
    result = []
    zero_count = 0

    for i in nums:
        if i != 0:
            result.append(i)
        else:
            zero_count += 1

    for _ in range(zero_count):
        result.append(0)

    return result

def q9(nums):

    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def q10(nums):
    nums2 = [1,3,5,7,9]
    result = []
    set_num2 = set(nums2)

    for num in nums:
        if num in set_num2:
            result.append(num)
    return result







