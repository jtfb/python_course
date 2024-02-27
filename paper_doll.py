def paper_doll(text):
    final_text = ""
    for char in text:
        final_text = final_text + char * 3
    print(final_text)


#Check
paper_doll("Hello")
paper_doll("Mississipi")