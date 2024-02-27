def master_yoda(text):
    splitted_text = text.split(" ")


    new_text = " ".join(splitted_text[::-1])


    print(new_text)

# Check
master_yoda('I am home')

# Check
master_yoda('We are ready too')