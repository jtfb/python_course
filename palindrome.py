def palindrome(s):


    reverse_text = s[::-1].replace(" ", "")


    print(reverse_text)

    if s == reverse_text:
        print("True")
    else:
        print("False")


palindrome('helleh')