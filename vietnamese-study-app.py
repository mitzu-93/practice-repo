import random
import vietnamese_words

select_deck = input('What set of cards do you want to study from? [Nouns/Fruits/Pronouns]').lower()

if select_deck == 'nouns':
    dictionary = vietnamese_words.vietnamese_nouns
elif select_deck == 'fruits':
    dictionary = vietnamese_words.vietnamese_fruits
elif select_deck == 'pronouns':
    dictionary = vietnamese_words.vietnamese_pronouns

english_to_vietnamese = {}

def start_flashcards():
    #retrieve separate key value pairs
    key = random.choice(list(dictionary.keys()))
    value = dictionary[key]

    #add reverse order to dictionary
    english_to_vietnamese[value] = key
    #pop dictionary
    del dictionary[key]

    user_answer = input(f'What is the translation for {key}?')
    if user_answer == value:
        print('Correct!')
        return True
    else:
        print(f'Wrong! The correct answer is {value}')
        return False   

# viet to eng counter
correct_viet = 0
incorrect_viet = 0

while dictionary:
    result_viet = start_flashcards()
    if result_viet:
        correct_viet += 1
    else:
        incorrect_viet += 1

accuracy_viet = correct_viet / (correct_viet + incorrect_viet) * 100

print(f'You got {correct_viet} correct out of {correct_viet + incorrect_viet}')
print(f'You got {incorrect_viet} correct out of {correct_viet + incorrect_viet}')
print(f'Your accuracy is {accuracy_viet}%')

#english to viet function
def english_flashcards():
    key_eng = random.choice(list(english_to_vietnamese.keys()))
    value_eng = english_to_vietnamese[key_eng]

    #pop dictionary
    del english_to_vietnamese[key_eng]

    user_answer = input(f'What is the translation for {key_eng}?')
    if user_answer == value_eng:
        print('Correct!')
        return True
    else:
        print(f'Wrong! The correct answer is {value_eng}')
        return False

#eng to viet counter
correct_eng = 0
incorrect_eng = 0

start_english = input('Do you want to study English to Vietnamese? [y/n]').lower()

if start_english == 'y':
    while english_to_vietnamese:
        result_eng = english_flashcards()
        if result_eng:
            correct_eng += 1
        else:
            incorrect_eng += 1
    
    accuracy_eng = correct_eng / (correct_eng + incorrect_eng) * 100
    
    print(f'You got {correct_eng} correct out of {correct_eng + incorrect_eng}')
    print(f'You got {incorrect_eng} correct out of {correct_eng + incorrect_eng}')
    print(f'Your accuracy is {accuracy_eng}%')

else:
    print('Goodbye, you studied well!')

