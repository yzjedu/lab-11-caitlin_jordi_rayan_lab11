# Programmers:  Caitlin Burns, Jordi Campoverde, Rayan Haq
# Course:  CS151, professor Zee
# Due Date: 11/28
# Lab Assignment:  11
# Problem Statement:  translates coded files into english
# Data In: dictionary file, file name
# Data Out: new file with translation
# Credits: read me file and class notes
# Input Files: morsecode.txt, morse1.txt, morse2.txt, morse3.txt

import os


# Purpose: allows user to select file to turn into dictionary
# Parameters: none
# Return: filename
def key_selection():
    filename = input('What file are you using to translate?: ')
    while filename != 'morsecode.txt':
        print('Invalid file. Try again.')
        filename = input('What file are you using to translate?: ')
    while not os.path.isfile(filename):
        print('Invalid file. Try again.')
        filename = input('What file are you using to translate?: ')
    return filename

# Purpose: converts file to dictionary
# Parameters: filename
# Return: m_d
def file_to_dictionary(filename):
    m_d = {}
    morse_data = open(filename, 'r')
    for line in morse_data:
        item = line.strip().split()
        key = item[1]
        val = item[0]
        m_d[key] = val
    morse_data.close()
    return m_d


# Purpose: allows user to select file to be translated
# Parameters: none
# Return: input_file
def inputfile():
    input_file = input('What file would you like to translate?: \nmorse1.txt\nmorse2.txt\nmorse3.txt\ntype selection here: ')
    while input_file != 'morse1.txt' and input_file != 'morse2.txt' and input_file != 'morse3.txt':
        print('Invalid file. Try again')
        input_file = input('What file would you like to translate?: \nmorse1.txt\nmorse2.txt\nmorse3.txt\ntype selection here: ')
    return input_file


# Purpose: translates file and creates and output file
# Parameters: key_selection, output_file, and m_d
# Return: none
def translate_file(key_selection, output_file, m_d):
    key_selection = open(key_selection, 'r')
    outfile = open(output_file, 'w')
    for line in key_selection:
        letters = line.strip().split()
        translation = []
        for letter in letters:
            if letter in m_d:
                translation.append(m_d[letter])
            else:
                translation.append('')
        outfile.write(' '.join(translation) + '\n')
    key_selection.close()
    outfile.close()


# Purpose: runs main program
# Parameters: none
# Return: none
def main():
    print('*' * 70)
    print('This program translates morse code into english using a dictionary')
    print('*' * 70)
    filename = key_selection()
    m_d = file_to_dictionary(filename)
    input_file = inputfile()
    translate_file(input_file, 'translation.txt', m_d)
    print('Your file has been translated into translation.txt file. Thanks!')


main()


