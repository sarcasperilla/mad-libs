#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 12:35:18 2018

@author: michaelcasper
"""

# A Mad Libs program that reads in text files and lets the user add their own
# text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file.

# Call mad_libs() function to play, with the argument being a
# txt file fomatted for Mad Libs (see first comment).

import string
import re
import os


# Split string from a text file and return a list of words
def textfile_to_list(textfile):
    """ Read text file and return a list of words & ending punctuation. """
    file = open(textfile, 'r')
    file_string = file.read()
    word_list1 = file_string.split()
    word_list2 = []
    word_list3 = []
    for word in word_list1:
        for c in string.punctuation:
            if c in word[-1]:
                word = word.split(c)
                word[1] = c
        word_list2.append(word)
    for main_entry in word_list2:
        if type(main_entry) is list:
            for thing in main_entry:
                word_list3.append(thing)
        elif type(main_entry) is str:
                word_list3.append(main_entry)
    return word_list3


# Loop through list of words and prompt user for input when needed
def take_user_input(word_list):
    """ Loop through word list prompt user to input part of speech. """
    madLibsRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    punctRegex = re.compile(r'[.,?!;:]')
    list_winputs = []
    list_winputs2 = []
    for word in word_list:
        try:
            match = madLibsRegex.search(word).group()
            if match == 'ADJECTIVE':
                userinput = input('Enter an adjective:\n')
            else:
                userinput = input('Enter a {0}:\n'.format(match.lower()))
            list_winputs.append(userinput)
        except AttributeError:
            list_winputs.append(word)
    for i in range(len(list_winputs)):
        try:
            match = punctRegex.search(list_winputs[i + 1]).group()
            combined = list_winputs[i] + list_winputs[i + 1]
            list_winputs2.append(combined)
        except AttributeError:
            if list_winputs[i] not in string.punctuation:
                list_winputs2.append(list_winputs[i])
            else:
                continue
        except IndexError:
            break
    completed_lib = ' '.join(list_winputs2)
    return completed_lib


# Open new txt file and write results of the mad libs & parint to screen
def write_txt(string, filename):
    """ Writes a string into a new textfile, which must be unqiue/new. """
    if not os.path.exists(filename):
        file = open(filename, 'w+')
        file.write(string)
        file.close()
    else:
        raise AttributeError("You already played this lib!")


# The one function to call them all
def mad_libs(madLibstxt):
    """ Takes a txt file formatted for Mad Libs and "plays" it! """
    completed_lib = take_user_input(textfile_to_list(madLibstxt))
    newfilename = '{0}_completed.txt'.format(madLibstxt[:-4])
    write_txt(completed_lib, newfilename)
    print()
    print(newfilename, "created!")
