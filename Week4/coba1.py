# A program to find the longest word in a given string

def find_longest_word(kalimat):
    """Find the longest word in the given sentence."""
    words = kalimat.split()  # Split the sentence into words
    longest_word = max(words, key=len)  # Find the word with the maximum length
    return longest_word

# Example usage
input_sentence = "I love to learn python"
longest_word = find_longest_word(input_sentence)
print(f'The longest word is "{longest_word}"')

# Example usage 2
input_sentence1 = "I am a python programmer"
longest_word = find_longest_word(input_sentence1)   
print(f'The longest word is "{longest_word}"')

print('\n--- Oleh L200234275 ---')