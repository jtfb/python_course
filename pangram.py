import string

def ispangram(str1, alphabet=string.ascii_lowercase):

    # set of the alphabet
    alphaset = set(alphabet)

    #removing spaces and making it lowercase
    str1_no_space = str1.lower().replace(" ", "")

    #set of str1
    str1_set = set(str1_no_space)


    if str1_set == alphaset:
        print("True")
    else:
        print("False")




    # output = ""
    #
    # for char in str1_no_space:
    #     output = output + char
    # print(output)


    # str1_lower = string.ascii_lowercase
    # print(str1_no_space)
    # print(set(alphabet))



ispangram("The quick brown fox jumps over the lazy dog")