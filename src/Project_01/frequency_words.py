# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# ○ Eg - line = “which is better python 2 or python 3”
# ○ Output – '2', 1
# '3', 1
# 'better', 1
# 'is', 1
# 'or', 1
# 'python', 2
# 'which', 1

from collections import Counter
import re


def frequency_words(input_text):
    # input: convert to lowercase and split into words
    words = re.findall(r'\b\w+\b', input_text.lower())

    # counting the frequency of each words
    frequency = Counter(words)

    # sort the words alphanumerically
    sorted_frequency = dict(sorted(frequency.items()))

    return sorted_frequency


def main():
    input_text = input("Enter Text: ")
    frequency = frequency_words(input_text)

    # Printing the frequency of each word
    for word, count in frequency.items():
        print(f"'{word}', {count}")


if __name__ == "__main__":
    main()
