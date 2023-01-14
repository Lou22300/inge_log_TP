# -*- coding: utf-8 -*-
"""This code only contains two functions to verify if a fasta file
only contains nucleotides."""

import os
# "os" is used here to verify if some files exist or not before using them in the function
import sys
# "sys" is used to put args to run the code in the terminal without any action of the user.

ADN_LIST=("A","C","G","T") # list of authorized nucelotides

def is_fasta(fastafile) : # takes in argument the name of the file
    """This function control if the file starts with a '>' used in fasta files headers."""
    if fastafile.split(".")[-1] in ["fasta","faa","fa"] : # extension is OK
        with open(fastafile, "r", encoding='UTF-8') as file :
            first_line = file.read(1) # take the first line of the file
            if first_line.split()[0] == ">" : # first char of first line
                return True # this looks like a fasta file
    return False

def adn_read(fastafile) : # takes in argument the name of the file
    """This function verifies if a fasta file only contains nucleotides."""
    with open(fastafile, "r", encoding='UTF-8') as file :
        line_counter = 0
        header = ""
        for line in file.readlines() : # verify line by line
            line_counter += 1
            if line[0] == ">" : # to fetch the header
                header = line.strip() # in a list
            else:
                line = line.strip() # to avoid errors with '\n'
                line = line.upper() # to avoide errors if 'acgt'
                column_counter = 0
                for char in line : # verify if each char is a nucleotide
                    column_counter += 1
                    if char not in ADN_LIST : # an error occurs
                        print("\n'" + char  + "' is not a nucleotide, in line " +
                        str(line_counter) + " and column " + str(column_counter)+
                        " for sequence '"+ header + "' in the file '" + fastafile +
                        "'.")

for arg in sys.argv:
    if os.path.isfile(arg) : # if file exists
        if str(arg).split(".",maxsplit=1)[-1] in ["fasta","faa","fa"] : # extension OK
            if is_fasta(arg) is True :
                adn_read(arg)
            else :
                print("\n'" + str(arg) + "' is not a fasta file (no headers).")
        else :
            print("\n'" + str(arg) + "' is not a fasta file (please check the extension).")
    else :
        print("\nError : the file '" + arg + "' doesn\'t exist.")
