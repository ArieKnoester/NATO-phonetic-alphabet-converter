import pandas


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for index, row in nato_alphabet_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# TODO 3. Add exception handling for non-alpha characters
while True:
    user_input = input("Enter a word: ")
    try:
        output = [nato_alphabet_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only characters in the alphabet are accepted.")
    else:
        print(output)
        break
