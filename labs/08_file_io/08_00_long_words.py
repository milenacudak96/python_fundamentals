'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
def characterCount():
    fin = open("words.txt")
    for line in fin:
        words = line.strip()
        if len(words) > 19:
            print(words)

characterCount()