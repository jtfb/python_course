def spy_game(nums):
    output = ""
    for numbers in nums:
        if numbers == 0:
            output = output + str(numbers)

        elif numbers == 7:
            output = output + str(numbers)

        else:
            pass

    # print(str(output))

    if output == "007":
        print("True")
    else:
        print("False")


# Check
spy_game([1, 2, 4, 0, 0, 7, 5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])
