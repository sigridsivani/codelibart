import sys

# 1
word_list = sys.argv 
word_list.pop(0)

sorted_words = sorted(word_list, key=str.lower)

print (sorted_words)
print(len(sorted_words))