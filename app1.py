# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:53:43 2020

@author: Sheheryar
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s?" % get_close_matches(word, data.keys())[0])
        user_input = input("Press Y for yes, press any other key for No\n")
        if user_input == 'Y' or user_input == 'y':
           return data[get_close_matches(word, data.keys())[0]]
        elif user_input == "N" or user_input == "n":
            return "Word doesnt exist, try again.!"
        else: 
            return "Invalid input"
    else:
        return "Word doesnt exist, try again."

word = input("Enter the word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item, end = "")
else:
    print(output)