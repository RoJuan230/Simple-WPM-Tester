import time
import os

def start_test():
    for num in [3, 2, 1]:    # countdown
        os.system('cls')
        print(f'{num}...')
        time.sleep(1)
        os.system('cls')

    start_time = time.time()
    words = input('Go! > ')
    elapsed = (time.time() - start_time)/60    # divide by 60 to get minutes.
    os.system('cls')
    time.sleep(2)

    words = words.split(' ')
    print(f'WPM: {len(words)/elapsed:.0f}')

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
    print('Type a phrase or two then hit enter to check out your WPM! You will start in 3 seconds')
    time.sleep(3.5)
    
    start_test()

welcome()

# TODO: make it so that the timer starts on a keypress.
