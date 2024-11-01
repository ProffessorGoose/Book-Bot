def count_words(text_string):
    word_count = len(text_string.split())
    return word_count

def count_characters(text_string):
    character_frequency_dict = {}
    for character in text_string:
        if character.isalpha():
            character = character.lower()
            if character in character_frequency_dict:
                character_frequency_dict[character] += 1
            else:
                character_frequency_dict[character] = 1
        else:
            continue
    return dict(sorted(character_frequency_dict.items()))


with open("books/frankenstein.txt", "r") as file:
    content = file.read()

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count_words(content)} words found in the document")

character_dict = count_characters(content)
for key, value in character_dict.items():
    print(f"the '{key}' character was found {value} times")

print("--- End report ----")
