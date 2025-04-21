from stats import number_of_words

def main():
    text = get_book_text("books/frankenstein.txt")
    words = number_of_words(text)   
    print(f"{words} words found in the document") 

    all_words = text.split()
    print("First 10 words:", all_words[:10])
    print("Last 10 words:", all_words[-10:])

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

if __name__ == "__main__":
    main()