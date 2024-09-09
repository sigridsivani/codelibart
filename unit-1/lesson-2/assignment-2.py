from unit1lesson2 import *
#1
number_list.sort()
# smallest_number = number_list[0]
#print(smallest_number)
#smallest number is 175

#2
#numbers_over_500 = [num for num in number_list if num > 500]

#smallest_number_over500 = numbers_over_500[0]
#print(smallest_number_over500)

#answer is 501


#3
#even_numbers = [x for x in number_list if x % 2 == 0]

#smallest_even_number = even_numbers[0]
#print(smallest_even_number)
#smallest even number is 176 

#4
#word_list.sort()
#number_of_words = len(word_list)
#print(number_of_words)
#print(word_list[49])

#the word is violation


#5
longest_word = word_list[0]

for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word

        print(longest_word)

        #the longest word is rehabilitation




     


