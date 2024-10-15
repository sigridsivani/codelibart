file = open("girlspilot-script.txt", "r")

word_counter = {}

words_avoid = ["a", "I", "to", "in", "of", "and", "her", "HANNAH","MARNIE", "JESSA","ADAM", "you", "is", "the","I'm", "you", "it"]

for line in file:
    for word in line.split():

        if word in words_avoid:
            continue

        if word in word_counter:
            word_counter[word] = word_counter[word]+1
            
        else:
            word_counter[word] = 1

top_10_words = sorted(word_counter.items(), key=lambda x: x[1], reverse=True) [:10]
#sorting words and creating tuples of word + count in dictionary
#key=lambda formula i copied from chatgpt in order to make the list in descending order
# [:10] for isolating the 10 first results

for word, count in top_10_words:
    print(f"{word}: {count}")


#I found that since its a script and most of the text is verbal its kinda hard to filter out all the filler words, as most of verbal dialogue is filler words
#I also noticed that when filtering out words you have to be spesific to capital letters and small, would be interesting to see if there is a way around that
#definetely feels abstract to me already a little bit, although it makes sense as I look at the examples of other peoples codes and put it in context of my own
#for some reason i get a little intimidated immediatelt when a for loop is involved, it feels like it gets big and scary and convoluted very quickly
# result no filters:
#the: 173
# a: 162
# I: 161
# HANNAH: 143
# to: 125
# you: 116
# in: 77
# of: 72
# and: 68
# her: 61
# result with filters: 
# I’m: 57
# my: 54
# (pause): 49
# You: 44
# have: 42
# LOREEN: 40
# like: 39
# that: 39
# just: 39
# for: 38

