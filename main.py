from stats import number_of_words
from stats import number_of_chars
from stats import sorted_dictionary

import sys

# Check if we have exactly two arguments (script name + book path)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# If we're here, then sys.argv[1] contains the book path
book_path = sys.argv[1]
# Now continue with the rest of your program...

def main():
    text = get_book_text(book_path)
    words = number_of_words(text)
    chars = number_of_chars(text)   
    

    print(f"{words} words found in the document")
    print(chars)

    sorted_chars = sorted_dictionary(chars)
     # Print the report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    
    # Print character count section
    print("--------- Character Count -------")
    
    # Loop through sorted characters and print if alphabetic
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Print footer
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

if __name__ == "__main__":
    main()