#!python3
"""
    Typing speed calculator from terminal
    Displays quotes and calculates your typing speed
    After each turn Press ENTER to continue, or Ctrl+C to quit
    Best result will be displayed after quitting
"""


import time,keyboard,random
from datetime import date
import colorama
from colorama import Fore, Back, Style,init


def accurecy_rating(accurecy):
    if accurecy == 100:
        return 5
    elif 70<=accurecy<=99:
        return 4
    elif 51<=accurecy<=69:
        return 3
    elif 19<=accurecy<=50:
        return 1
    elif 1<=accurecy<=19:
        return 1
    else:
        return 0

def calculate_correct_letters(original_text, typed_text):
    correct_letters = 0
    index = 0
    try:
        for char in original_text:
            if char == typed_text[index]:
                correct_letters +=1
            index+=1
    except IndexError:
        pass
    return correct_letters


def typing_test():
    start_time = time.time()
    typed_text = input(">>")
    end_time = time.time()
    time_spent = round(end_time-start_time,2)
    return typed_text,time_spent


def display_results(speed, total_letters, correct_letters,accurecy):
    print(Style.RESET_ALL,"="*50)
    print(Fore.CYAN,f"your speed is {speed} WPM\n"
                    f" you got {correct_letters}/{total_letters} correct characters",Style.RESET_ALL)
    print(Fore.YELLOW,"*"*accurecy_rating(accurecy),Style.RESET_ALL)
    print(Style.RESET_ALL,"="*50)


if __name__ == "__main__":
    quotes = open(r'C:\TEXT\FILE\PATH\IN\YOUR\DEVICE\quotes.txt').read().split('\n')    # Enter you file path HERE to get the quotes
    scores = []
    input("To START press Enter, to END press Ctrl+C\n")
    while True:
        colorama.init()
        try:
            quote = random.choice(quotes)
            print(Back.CYAN," "+quote,Style.RESET_ALL)                    # Print quote with Cyan background

            typed_text,time_spent = typing_test()

            correct_letters = calculate_correct_letters(quote,typed_text)
            total_letters = len(quote)

            speed = round((len(typed_text)/5)/(time_spent/60),2)
            accurecy = round((correct_letters/len(quote))*100)

            scores.append(speed)

            display_results(speed, total_letters, correct_letters, accurecy)

            input("\nContinue?\n")                                        # press ENTER to continue
        except KeyboardInterrupt:                                         # when Ctrl+C is presses
            best_score = max(scores)
            print(Back.GREEN,f"Your best score was {best_score} \n Keep going! ",Style.RESET_ALL)
            break
