def animal_crackers(text):
    splitted_text = text.split(" ")

    if splitted_text[0][0].lower() == splitted_text[1][0].lower():
        print ("True")
    else:
        print ("False")


#check
animal_crackers("Levelhead Llama")
animal_crackers("Crazy Kangaroo")