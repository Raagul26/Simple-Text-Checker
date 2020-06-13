# Simple Text Checker

# Author: Raagul26
# Text Checker is a simple program to count and finder letters and words in a text file
# It only works on .txt file. For other formats may be updated in future. Stay tuned.

# Import module
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
    print("Text-Checker".center(50, "-"))
    print("1.Word Counter\n2.Letter Counter\n3.Word Finder\n4.Letter Finder\n5.Exit")
    print("".center(50, "-"))
    choice = input("\nEnter your choice: ")
    while not choice.isnumeric():
        print("\nEnter correctly...")
        choice = input("Enter your choice: ")

    path = loc()
    # Word count
    if choice == '1':
        with open(path) as file:
            r = file.read()
            list_words = r.split()
            # print(list_words)
            words = len(list_words)
            print("Total no of words:", words)

    # Letter count
    if choice == '2':
        with open(path) as file:
            r = file.read()
            list_letters = list(r)
            list_letters = [elem for elem in list_letters if elem.strip()]
            letters = len(list_letters)
            print("Total no of letters:", letters)

    # Word finder
    if choice == '3':
        find = input("Enter search Word: ")
        fi = set()
        with open(path) as file:
            r = file.read()
            ls = r.split()
            print()
            for i in range(len(ls)):
                if find == ls[i].lower():
                    fi.add(i + 1)
            if len(fi) > 0:
                print("Word found at location :", fi)
            else:
                print("'''Not found'''")

    # Letter finder
    if choice == '4':
        find = input("Enter search letter: ")
        fi = set()
        with open(path) as file:
            r = file.read()
            ls = list(r)
            print()
            for i in range(len(ls)):
                if find == ls[i].lower():
                    fi.add(i + 1)
            if len(fi) > 0:
                print("Letter found at location :", fi)
            else:
                print("'''Not found'''")

    # Exit
    if choice == '5':
        print()
        print("EXIT".center(50, "*"))
        exit(0)

    cont = input("\nPress enter to continue...")
    os.system('cls' if os.name=='nt' else 'clear')
