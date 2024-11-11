import requests
from bs4 import BeautifulSoup
import os
import markovify
import re #import regular expression
# import fitz

directory = "corpus-scripts" #direct to the right folder



# goodfellas_response = requests.get("http://www.script-o-rama.com/movie_scripts/g/goodfellas-script-transcript.html")
meangirls_response = requests.get("https://www.dailyscript.com/scripts/mean_girls.pdf")
# goodfellas_soup_html = BeautifulSoup(goodfellas_response.text, "html.parser")
meangirls_soup_html = BeautifulSoup(meangirls_response.text, "html.parser")
# goodfellas_text = goodfellas_soup_html.get_text()
meangirls_text = meangirls_soup_html.get_text() 

# file_path = os.path.join(directory, 'goodfellas-script.txt') #open directory

# with open(file_path, "w") as goodfellas_data:
#     goodfellas_data.write(goodfellas_text) #turning the data into text



# meangirls_data = open('meangirls-script.txt', 'w')
# meangirls_data.write(meangirls_text)
# meangirls_data.close()
    #was NOT working

# def pdf_to_txt(pdf_path, txt_path):
#     pdf = fitz.open(pdf_path)

#     with open(txt_path, "w", encoding="utf-8") as txt_file:
#         for page_num in range(pdf.page_count):
#             page = pdf[page_num]
#             text = page.get_text("text")
#             txt_file.write(text)


# pdf_to_txt("meangirls-script.pdf", "meangirls-script.txt")
    #   Second attempt, still not working, error accesing the pdf
    # unfortunately i have to cheat and make my own text file

#Now i have my two txt files!


with open("corpus-scripts/meangirls-script.txt") as f:
    meangirls_text = f.read()
# with open("corpus-scripts/goodfellas-script.txt") as f:
#     goodfellas_text = f.read() 
    #open both files make then available in read format
    

character_lines_mg = re.findall(r"^([A-Z]+(?:\s[A-Z]+)*)\n(.*?)(?=\n[A-Z]+\s*\n|\Z)", meangirls_text, re.MULTILINE | re.DOTALL)
# character_lines_gf = re.findall(
#     r"^(?P<character>[A-Z\s]+(?:\(CONT'D\))?)\s*\n(?:\((?:[^\)]+)\)\s*)*(?P<dialogue>[^A-Z][^\n]*(?:\n(?![A-Z]{2,}).*)*)",
#     goodfellas_text,
#     re.MULTILINE)






#this is a regular expression from chatgpt that identifies exactly what are character lines in the scripts 

female_names_mg = ["CADY", "REGINA", "GRETCHEN","KAREN", "JANIS",]
male_names_mg = ["AARON", "KEVIN GNOR","SHANE"]
#create lists of female and male names"
# female_names_gf = ["CONNIE", "SANDRA", "WOMAN'S VOICE", "CARMELLA", "WOMAN"]
# male_names_gf = ["BONANSERA", "VITO CORLEONE", "MICHAEL","TESSIO", "TOM", "SONNY", "CLEMENZA", "FREDO"]

female_dialogue_mg = []
male_dialogue_mg = []
#creating empty lists for where the dialogue will go
# female_dialogue_gf = []
# male_dialogue_gf = []

for character, dialogue in character_lines_mg:
    lines = dialogue.splitlines()
    if len(lines) > 1:
        dialogue = lines[0].strip() #take the first line only 
    if character in female_names_mg:
        female_dialogue_mg.append(dialogue.strip())
    elif character in male_names_mg:
        male_dialogue_mg.append(dialogue.strip())
 #for loop that seperates male and female dialogue from eachother and puts it into respective lis
 


all_f_dialogue_mg= "\n".join(female_dialogue_mg)
all_m_dialogue_mg= "\n".join(male_dialogue_mg)
#puts all the lines of each gender in a string so that it can be individually interperted by markovify

# for character, dialogue in character_lines_gf:
#     lines = dialogue.splitlines()
#     if len(lines) > 1:
#         dialogue = lines[0].strip()  #take the first line only
#     if character in male_names_gf:
#         male_dialogue_gf.append(dialogue.strip())
#     elif character in female_names_gf:
#         female_dialogue_gf.append(dialogue.strip())

# all_f_dialogue_gf= "\n".join(female_dialogue_gf)
# all_m_dialogue_gf= "\n".join(male_dialogue_gf)

# print(male_dialogue_gf)

generated_cady = markovify.NewlineText(all_f_dialogue_mg, state_size=1)
generated_aaron = markovify.NewlineText(all_m_dialogue_mg, state_size=1)
 #markovify
 #markovify.newlinetext instead of just .text because it is spesifcially designed for text structured line by line
# generated_henry = markovify.NewlineText(all_m_dialogue_gf)
# generated_karen = markovify.NewlineText(all_f_dialogue_gf)

conversation_meangirls = []
last_speaker = None 
for i in range(45):
    if last_speaker != "CADY":
        female_sentence_mg = generated_cady.make_sentence()
        if female_sentence_mg:
            conversation_meangirls.append(f"CADY: {female_sentence_mg}")
            last_speaker = "CADY"
            continue

    male_sentence_mg = generated_aaron.make_sentence()
    if male_sentence_mg:
        conversation_meangirls.append(f"AARON: {male_sentence_mg}")      
        last_speaker = "AARON"


# conversation_goodfellas = []
# for i in range(50):
#     if last_speaker != "HENRY":
#         male_sentence_gf = generated_henry.make_sentence()
#         if male_sentence_gf:
#             conversation_goodfellas.append(f"HENRY: {male_sentence_gf}")
#             last_speaker = "HENRY"
#             continue

#     female_sentence_gf = generated_karen.make_sentence()
#     if female_sentence_gf:
#         conversation_goodfellas.append(f"KAREN: {female_sentence_gf}")      
#         last_speaker = "KAREN"



print("\n\n\n")
print("MEAN GIRLS (2004)" + "\n")
print("\n".join(conversation_meangirls))  # print each line separately
print("\n\n")


# print("\n\n\n")
# print("GOODFELLAS (1990)" + "\n")
# print("\n".join(conversation_goodfellas))  # print each line separately
# print("\n\n")


