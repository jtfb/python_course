def ran_check(num,low,high):
    list_range = range(low,high+1)

    if num in list_range:
        print("{} is in range between 2 and 7".format(num))
    else:
        print("Try another one")

    print(list_range)


# Check
ran_check(2, 2, 7)