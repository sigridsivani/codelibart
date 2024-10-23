import markovify
# # look at documentation for markofivy here: https://github.com/jsvine/markovify

text = open("crgslist_acting.txt").read()

generator = markovify.Text(text) 

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(80))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")