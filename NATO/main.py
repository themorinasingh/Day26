import pandas

#TODO 1. Create a dictionary in this format:
# example dict : {"A": "Alfa", "B": "Bravo"}

file_data = pandas.read_csv("nato_phonetic_alphabet.csv")

part_1_dict = {data.letter: data.code for (index, data) in file_data.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

#writing a function to decode the word

def nato_alphabet_maker():
    word = input("Enter a Word: ").upper()

    nato_alphabet_for_word = [part_1_dict[alphabet] for alphabet in word]

    return nato_alphabet_for_word


print(nato_alphabet_maker())
