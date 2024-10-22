import markovify

text = open("SJM-wikipedia.txt").read()

generator = markovify.Text(text)

paragraph = ""

for i in range(10):
    paragraph += str(generator.make_short_sentence(200))
    paragraph += " "

print("\n\n\n")
print(paragraph)
print("\n\n\n")

