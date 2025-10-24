import string

def compute_frequencies(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    words = text.split()
    clean_words = []
    count = 0
    for word in words:
        newWord = word.strip(string.punctuation)
        clean_words.append(newWord)
        print(count)
        count = count + 1
    # print(clean_words)
    print(count)

compute_frequencies("../TextFiles/alice.txt")



