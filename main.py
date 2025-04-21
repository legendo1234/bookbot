def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)    

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

if __name__ == "__main__":
    main()