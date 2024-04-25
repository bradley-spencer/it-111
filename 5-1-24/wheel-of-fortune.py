#!/usr/bin/env python3

word = "abracadabra"

guess = []

def print_current():
    for letter in word:
        if letter in guess:
            print(letter, end = "")
        else:
            print("-", end = "")
    print()

def main():
    num_guesses = 0
    letters = set(word)
    while not letters.issubset(set(guess)):
        print_current()
        current = input("Guess a letter: ")
        guess.append(current)
        print(f"The letter '{current}' appears {word.count(current)} times.")
        num_guesses += 1

    print("You won in", num_guesses, "guesses! The word was:", word)

main()
