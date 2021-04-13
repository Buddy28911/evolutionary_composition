# Main file for Danny Noe's Evolutionary Music Project

from music_data import *

def set_key_signature():
    print(KEY)
    print("The default key signature is ")
    # yes_no = input("Would you like to change the key signature?")
    # yes_no = yes_no.lower()
    key_change = False

    while True:
        yes_no = input("Would you like to change the key signature?")
        yes_no = yes_no.lower()
        if yes_no == "yes" or yes_no == "y" or yes_no == "no" or yes_no == "n":
            if yes_no == "yes" or yes_no == "y":
                key_change = True
            break
        else:
            print("Unknown response")

    if key_change:
        print("Available key signatures:")
        print(SCALES.keys())
        while True:
            new_key = input("Desired key signature?")
            if new_key in SCALES.keys():
                #KEY = new_key
                break
            else:
                print(new_key, " unsupported.")

def main():
    print("Welcome to the evolutionary composition program!")
    set_key_signature()
    print(KEY)


main()