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

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]


def get_sorted_num_list(num_characters):
    sorted_num_list = []
    # for each key/value (char:num) pair, create a new dictionary and add it to the list
    for char in num_characters:
        num = num_characters[char]
        sorted_num_list.append({"char": char, "num": num})
    # sort the list with the highest number in decending order
    sorted_num_list.sort(reverse=True, key=sort_on)

    return sorted_num_list