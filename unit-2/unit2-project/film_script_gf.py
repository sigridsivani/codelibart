import requests
from bs4 import BeautifulSoup
import os
import markovify
import re #import regular expression

directory = "corpus-scripts" #direct to the right folder

# goodfellas_response = requests.get("http://www.script-o-rama.com/movie_scripts/g/goodfellas-script-transcript.html")
# goodfellas_soup_html = BeautifulSoup(goodfellas_response.text, "html.parser")
# goodfellas_text = goodfellas_soup_html.get_text()

# file_path = os.path.join(directory, 'goodfellas-script.txt') #open directory

# with open(file_path, "w") as goodfellas_data:
#     goodfellas_data.write(goodfellas_text) #turning the data into text

with open("corpus-scripts/goodfellas-script.txt") as f:
    goodfellas_text = f.read() 
    #open file make then available in read format

character_lines_gf = re.findall(r"([A-Z\s]+)\n([^\n]+)", goodfellas_text)


# Regex pattern to capture character names 
character_name_pattern = r"(?m)^[A-Z][A-Z\s]+(?=\n)"

# Find all unique character names
character_names = set(re.findall(character_name_pattern, goodfellas_text))
sorted_character_names = sorted(character_names)

# Separate names into male and female lists (initially all will be empty)
male_characters = []
female_characters = []

# Manually categorize names (this list is based on character familiarity and may need adjustments)
# Add character names to each list based on known gender
known_male_characters = {"HENRY", "JAMES", "TOMMY", "BATTS", "PAUL", "JIMMY", "SONNY", "TUDDY", "BRUCE", "MAURICE"}
known_female_characters = {"KAREN", "MICKEY", "ANGIE", "HELENE", "CARMELLA"}

for name in sorted_character_names:
    if name in known_male_characters:
        male_characters.append(name)
    elif name in known_female_characters:
        female_characters.append(name)

female_dialogue_gf = []
male_dialogue_gf = []


for character, dialogue in character_lines_gf:
    dialogue = dialogue.strip()
    if dialogue:
        if character in known_male_characters:
            male_dialogue_gf.append(dialogue)
        elif character in known_female_characters:
            female_dialogue_gf.append(dialogue)

all_f_dialogue_gf= "\n".join(female_dialogue_gf)
all_m_dialogue_gf= "\n".join(male_dialogue_gf)


# print(all_m_dialogue_gf)
# print(all_f_dialogue_gf)

if all_m_dialogue_gf:
    generated_henry = markovify.NewlineText(all_m_dialogue_gf, state_size=1)
else:
    print("No male dialogue found.")

if all_f_dialogue_gf:
    generated_karen = markovify.NewlineText(all_f_dialogue_gf, state_size=1)
else:
    print("No female dialogue found.")
 
last_speaker = None
conversation_goodfellas = []
for i in range(45):
    if last_speaker != "HENRY" and generated_henry:
        male_sentence_gf = generated_henry.make_sentence()
        if male_sentence_gf:
            conversation_goodfellas.append(f"HENRY: {male_sentence_gf}")
            last_speaker = "HENRY"
            continue

    if generated_karen:
        female_sentence_gf = generated_karen.make_sentence()
        if female_sentence_gf:
            conversation_goodfellas.append(f"KAREN: {female_sentence_gf}")
            last_speaker = "KAREN"

print("\n\n\n")
print("GOODFELLAS (1990)" + "\n")
print("\n".join(conversation_goodfellas))  # print each line separately
print("\n\n")


