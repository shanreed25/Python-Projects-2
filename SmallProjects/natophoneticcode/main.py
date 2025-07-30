import pandas
# Create a tool that takes the NATO phonetic alphabet which is generated because it is often
# really important for the other side to know exactly what it is that you said and
# which letters you are spelling out so that they do not mistake your E for a B or T for a C

# # Solution-1********************************************************************************************
# #TODO 1. Create a dictionary from the nato_phonetic_alphabet.csv in this format:
# nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# # print(nato_data_frame)
#
# nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
# print(nato_dict)
# # {"A": "Alfa", "B": "Bravo"}
#
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input("Enter A Word: ").upper()
# phonetic_code_words = [nato_dict[user_letter] for user_letter in user_input]
# print(phonetic_code_words)

# With Exception handling****************************************************************************************
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


nato_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_dict)


def generate_code_words():
    user_input = input("Enter A Word: ").upper()
    try:
        phonetic_code_words = [nato_dict[user_letter] for user_letter in user_input]
    except KeyError:
        print("Sorry only letters in the alphabet accepted")
        generate_code_words()
    else:
        print(phonetic_code_words)
        
        
generate_code_words()



























# Solution-2********************************************************************************************
# # TODO 1. Create a dictionary from the nato_phonetic_alphabet.csv in this format:
# nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# # print(nato_data_frame)

# nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}
# print(nato_dict)
# # {"A": "Alfa", "B": "Bravo"}

# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# user_input = input("Enter A Word: ").upper()
# user_input_list = [letter for letter in user_input]
# phonetic_code_words = []
# #Looping through dictionaries:
# for l in user_input:
#     code_dict = {letter: code for (letter, code) in nato_dict.items() if l == letter}
#     for (key, value) in code_dict.items():
#         phonetic_code_words.append(value)
# print(phonetic_code_words)