def minion_game(string):

    a_name = 'Stuart'
    b_name = 'Kevin'
    letter_list = [a for a in string]


    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = [a for a in string if a not in vowels]


    a_words = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i] not in vowels]
    b_words = [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i] in vowels]


    a_score = len(a_words)
    b_score = len(b_words)


    if a_score > person_b_score:
        print(f"{a_name} wins with a score of {a_score}!")
    elif b_score > person_a_score:
        print(f"{b_name} wins with a score of {b_score}!")
    else:
        print("It's a tie!")

word = input("enter the word: ").upper()
minion_game(word)

