def number_of_words(text):
    # Try splitting by whitespace to get all words
    words = text.split()
    return len(words)

def number_of_chars(sentence):
    new_dict = {}
    for char in sentence:
        lower_char = char.lower()  # Convert to lowercase
        if lower_char not in new_dict:
            new_dict[lower_char] = 1
        else:
            new_dict[lower_char] += 1
    return new_dict

def sorted_dictionary(chars):
    dict_to_list = []

    def sort_on(dict):
        return dict["count"]
    
    for char, count in chars.items():  # Use .items() to get both key and value
        # Create a dictionary for this character and count
        char_dict = {"char": char, "count": count}
        # Append that dictionary to our list
        dict_to_list.append(char_dict)
    
    # Sort the list in place
    dict_to_list.sort(reverse=True, key=sort_on)
    
    # Return the sorted list
    return dict_to_list