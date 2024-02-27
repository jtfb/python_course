def almost_there(number):
    if abs(100-number) <= 10 or abs(200 - number) <= 10:
        # return True
        print("True")
    else:
        print("False")



# Check
almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)