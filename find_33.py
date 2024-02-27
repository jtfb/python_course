def has_33(nums):
    i = 0
    print(len(nums))

    for numbers in nums:
        while i < len(nums) + 1:
            # if nums[i] == 3 and nums[i+1] == 3:
            #     i = i + 1
            #     print("True")
            if nums[i] == nums[i+1]:
                i = i + 1
                print("True")
            else:
                if i > len(nums) + 1:
                    pass
                else:
                    i = i + 1
                    print("False")



# Check
has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3])