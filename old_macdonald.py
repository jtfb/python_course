def old_macdonald(text):

    new_text = ""

    new_text = text.capitalize()
    print("new text is {}".format(new_text))

    final_text = new_text[0:3] + new_text[3].upper() + new_text[4:]

    print(final_text)

# Check
old_macdonald('macdonald')