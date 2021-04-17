'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''


def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


def shortest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    min_len = len(min(words, key=len))
    return [word for word in words if len(word) == min_len]


print(longest_word('words.txt'))
print(shortest_word('words.txt'))


def count(filename):
    num_words = 0
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            num_words += len(words)
    print("Number of words:")
    print(num_words)


count('words.txt')
