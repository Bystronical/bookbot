import os

def main():
    #print("Current working directory:", os.getcwd(), file=open('debug.log', 'w'))
    #print("Files in current directory:", os.listdir(), file=open('debug.log', 'a'))

    book_file_name = "frankenstein.txt"
    with open(f"books/{book_file_name}") as f:
        file_contents = f.read()
        #print(file_contents)

    print(f"--- Begin report of {book_file_name} ---")

    num_words = count_words(file_contents)
    print(num_words, "words found in the document")

    frequency = char_frequency(file_contents)
    for k,v in frequency.items():
        print(f"'{k} found {v} times")

    print("--- End Report ---")

def count_words(text):
    words = text.split()
    return len(words)

def char_frequency(text):
    lowered_text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequency_count = {}
    for letter in lowered_text:
        if letter in alphabet:
            if letter in frequency_count:
                frequency_count[letter] += 1
            else:
                frequency_count[letter] = 1

    sorted_frequency = dict(sorted(frequency_count.items(), key=lambda item: item[1], reverse=True))


    return sorted_frequency


main()
