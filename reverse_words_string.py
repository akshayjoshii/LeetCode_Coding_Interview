# Implementation of multiple strings/character reversal tasks in a a sentence

# Complexity: Time & Space: O(n)
# Space complexity could be reduced to O(1) by swapping the words in-place

def sentenceReverse(string):
    words_reversed = []
    middle_words_reversed = []
    all_words_reversed = []
    word_list = string.split(' ')
    for i, word in enumerate(word_list):
        words_reversed.insert(0, word)
        all_words_reversed.append(word[::-1])
        if i == 0 or i == (len(word_list) - 1):
            middle_words_reversed.append(word)
        else:
            middle_words_reversed.append(word[::-1])

    return words_reversed, middle_words_reversed, all_words_reversed

s = input("Please enter a string:\n")
print(f"Original Sentence: \"{s}\"")

task_1, task_2, task_3 = sentenceReverse(s)

# Task 1: Word order reversed in a sentence
print(f"Reversed Sentence: \"{' '.join(task_1)}\"")

# Task 2: Reverse characters of middle words of a string
print(f"Reversed characters of middle words: \"{' '.join(task_2)}\"")

# Task 2: Reverse characters of all words of a string
print(f"Reverse characters of all word: \"{' '.join(task_3)}\"")