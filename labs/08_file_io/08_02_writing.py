'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
with open('words.txt') as rf, open('reversed.txt', 'w') as wf:
    for line in reversed(rf.readlines()):
        wf.write(line)