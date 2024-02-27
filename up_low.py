def up_low(s):

    upper_count = 0
    lower_count = 0

    print(len(s))

    for char in s:
        if char.isupper():
            upper_count = upper_count + 1
        elif char.islower():
            lower_count = lower_count + 1
        else:
            pass

    print("No. of Upper case characters: {}".format(upper_count))
    print("No. of Lower case characters: {}".format(lower_count))

    print(len(s))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)