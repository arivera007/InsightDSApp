## Author: Adriana Rivera
## Subject: Program that counts the total number of words or numbers in a group of files
## Input: Only files located in a directory called wc_input
## Output: One file called wc_results in a directory called wc_output
## Assumptions
## Ignore the case, cat == Cat, so in the dictionary everything will be lowercase.
## We want to count numbers as well.
## Given the hash nature of Dictionary, storing sorting data is not needed and is wasteful, so sorting is only used for dispalying

import sys
import re           # Regular Expressions Library
from os import listdir
from os.path import isfile, join


def wordCountFile(fileName):
    myFile = open(fileName)
    expression = re.compile(r"[\w]+")   # Supposed to be faster if the regulr expression is precompiled (\w is for alphanumeric characters)
    for line in myFile:                 # Only one line in memory at a time. 
        for word in expression.findall(line):
            word = word.lower()
            scores[word] = scores.get(word, 0) + 1
    myFile.close()

def createResultsFile(fileName):            
    f = open(fileName,'w')
    for key in sorted(scores):          # Dictionaries use hash table for fast access, so sorting is only used at displaying time.
        f.write("%s: %s \n" % (key, scores[key]))
    f.close()


def main():
    global scores
    scores = {}                     # initialize an empty dictionary
    INPUT_DIR = sys.argv[1]
    OUTPUT_PATH = sys.argv[2]
    for f in listdir(INPUT_DIR) :   #for each file in the directory
        currentPath = join(INPUT_DIR,f)
        if isfile(currentPath):
            wordCountFile(currentPath)  #Count the words
    createResultsFile(OUTPUT_PATH)             # Create the final file with all the results.

if __name__ == '__main__':
    main()