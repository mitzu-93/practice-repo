import random
import vietnamese_words

english_to_vietnamese = {}

def start_flashcards():
    #retrieve separate key value pairs
    key = random.choice(list(vietnamese_words.vietnamese_fruits.keys()))
    value = vietnamese_words.vietnamese_fruits[key]

    #add reverse order to dictionary
    english_to_vietnamese[value] = key
    #pop dictionary
    del vietnamese_words.vietnamese_fruits[key]

    user_answer = input(f'What is the translation for {key}?')
    if user_answer == value:
        print('Correct!')
        return True
    else:
        print(f'Wrong!')
        return False   

# viet to eng counter
correct_viet = 0
incorrect_viet = 0

while vietnamese_words.vietnamese_fruits:
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
        print(f'Wrong!')
        return False

#eng to viet counter
correct_eng = 0
incorrect_eng = 0

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
