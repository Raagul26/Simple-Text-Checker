# Simple Text Checker

# Author: Raagul26
# Text Checker is a simple program to count and find letters and words in a text file.
# It works only on .txt file. For other formats may be updated in future. Stay Tuned.

import os


# Function to get path
def loc():
    path = input("Enter file name (File_name.txt): ")
    if os.path.exists(path):
        return path
    else:
        while True:
            if os.path.exists(path):
                break
            else:
                print("\nFile not exists...")
                path = input("Enter file name: ")
        return path


print("Note: Only works on text file")

# Main program starts here
while True:
    print('''
      _______ ________   _________    _____ _    _ ______ _____ _  ________ _____  
     |__   __|  ____\ \ / /__   __|  / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
        | |  | |__   \ V /   | |    | |    | |__| | |__ | |    | ' /| |__  | |__) |
        | |  |  __|   > <    | |    | |    |  __  |  __|| |    |  < |  __| |  _  / 
        | |  | |____ / . \   | |    | |____| |  | | |___| |____| . \| |____| | \ \ 
        |_|  |______/_/ \_\  |_|     \_____|_|  |_|______\_____|_|\_\______|_|  \_\\
        
        ''')
    print(" 1.Word Counter\n 2.Letter Counter\n 3.Word Finder\n 4.Letter Finder\n 5.Exit")
    print("".center(80, "-"))
    choice = input("\nEnter your choice: ")
    while not choice.isnumeric():
        print("\nEnter correctly...")
        choice = input("Enter your choice: ")

    # Word count
    if choice == '1':
        path = loc()
        with open(path) as file:
            print('Processing...')
            r = file.read()
            list_words = r.split()
            words = len(list_words)
            print("Total no of words:", words)

    # Letter count (Including punctuations)
    if choice == '2':
        path = loc()
        with open(path) as file:
            print('Processing...')
            r = file.read()
            list_letters = list(r)
            list_letters = [elem for elem in list_letters if elem.strip()]  # elem cannot be false
            letters = len(list_letters)
            print("Total no of letters:", letters)

    # Word finder
    if choice == '3':
        path = loc()
        find = input("Enter search Word: ")
        fi = set()
        with open(path) as file:
            print('Processing...')
            r = file.read()
            ls = r.split()
            print()
            for i in range(len(ls)):
                if find == ls[i].lower():
                    fi.add(i + 1)
            if len(fi) > 0:
                print("Word found at location :", sorted(fi))  # prints all occurrences
            else:
                print("'''Not found'''")

    # Letter finder
    if choice == '4':
        path = loc()
        find = input("Enter search letter: ")
        fi = set()
        with open(path) as file:
            print('Processing...')
            r = file.read()
            ls = list(r)
            print()
            for i in range(len(ls)):
                if find == ls[i].lower():
                    fi.add(i + 1)
            if len(fi) > 0:
                print("Letter found at location :", sorted(fi))  # prints all occurrences
            else:
                print("'''Not found'''")

    # Exit
    if choice == '5':
        print()
        print("EXIT".center(50, "*"))
        exit(0)

    input("\nPress enter to continue...")
    os.system("cls" if os.name="nt" else "clear")
