def unique_list(lst):

    i = 0
    new_list = [lst[0]]
    print(new_list)

    for num in lst:
        if num not in new_list:
            new_list.append(num)


    print(new_list)

lst = ([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
unique_list(lst)