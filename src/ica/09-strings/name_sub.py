def count_word (word, text):
    split_text = text.split()
    # return split_text.count(word)
    count = 0
    for i in split_text:
        if i == word:
            count = count + 1
    return count

sallie = count_word("Juliana,", "Her name is Juliana, I love pancakes")
print (sallie)
