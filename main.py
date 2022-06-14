import time
import os
import msvcrt

def start_test():
    print('> ')
    first_letter = msvcrt.getch()    # Wait until character is typed.
    os.system('cls')    # clear console
    start_time = time.time()    # Once the first letter is recorded, start.

    words = input(f'> {str(first_letter)[2:3]}')
    elapsed = (time.time() - start_time)/60    # divide by 60 to get minutes.
    os.system('cls')
    time.sleep(2)

    adjusted_words_len = (len(words) + 1)/5    # word is defined as every five characters in this case.
    print(f'WPM: {adjusted_words_len/elapsed:.0f}')

    play_again = input('Would you like to play again? ')    

    if (play_again.strip()).lower() == 'yes' or (play_again.strip()).lower() == 'y':
        start_test()
    else:
        return
    

def welcome():
    os.system('cls')
    print('Welcome to the WPM tester!!')
    time.sleep(2.5)
    os.system('cls')
    print('Type a phrase or two then hit enter to check your WPM...')
    time.sleep(2)
    os.system('cls')

    start_test()

welcome()
