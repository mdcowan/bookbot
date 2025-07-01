def get_num_words(book_text):
    words_list = book_text.split()
    num_words = len(words_list)
    return num_words

def get_num_characters(book_text):
    #variable to hold the character count dictionary
    num_characters = {}
    # convert the string to all lower case
    new_book_text = book_text.lower()
    # loop through each character in the string
    for char in new_book_text: 
        # if the character is on the dictonary, increase the count
        # otherwise add the character to the dictionary and set the count to 1
        if char in num_characters:
            num_characters[char] += 1
        else: 
            num_characters[char] = 1
    return num_characters
            