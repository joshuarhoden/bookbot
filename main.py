def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_words = get_number_words(text)
    lower_string = lower_case(text)
    characters = character_count(lower_string)
    sorted_alpha = report(characters, number_words)

    

def report(characters, number_words):
    sorted_characters = dict(sorted(characters.items(), reverse=False))
    sorted_alpha_characters = []
    for character, amount in sorted_characters.items():
        if character.isalpha() == True:
            sorted_alpha_characters.append({"character": character, "amount": amount})
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_words} words found in the document")
    for character_dict in sorted_alpha_characters:
        print(f"The '{character_dict['character']}' character was found {character_dict['amount']} times")
    print("--- End report ---")
    
    
    




def get_number_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def lower_case(text):
    return text.lower()
    
def character_count(lower_string):
    char_count = {}
    for character in lower_string:
        if character in char_count:
           char_count[character] += 1
        else:
           char_count[character] = 1
    return char_count




main()
    