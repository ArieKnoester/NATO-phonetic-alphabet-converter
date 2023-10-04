import pandas


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for index, row in nato_alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
output = [nato_alphabet_dict.get(char.upper()) for char in user_input]
print(output)
