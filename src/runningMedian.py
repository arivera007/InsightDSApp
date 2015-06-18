## Author: Adriana Rivera
## Subject: Running Median of text files. Program that calculates the median of the numbers of words in each line
## Input: All the files located in a directory called wc_input
## Output: One file called med_result in a directory called wc_output with the accumulated median of the number of words in the lines.
## Assumptions:
##   The output file needs to be updated every time a line is visited, functioning like a log,
## as oposed to creating at the end all at once which would be more efficient.

import sys
import re           # Regular Expressions Library
from os import listdir
from os.path import isfile, join
import statistics


def calcMedian(fileName):
    """ Loads one file at a time and calculates the size in words for each line and calcualtes the median for all the lines so far,
    then writes them right away in a log file.
    """
    myFile = open(fileName)
    expression = re.compile(r"[\w]+")   # Supposed to be faster if the regulr expression is precompiled (\w is for alphanumeric characters)
    for line in myFile:                 # Only one line in memory at a time. 
        lineWordsAmount.append(len(expression.findall(line)))
        medianFile.write("  %s \n" % statistics.median(lineWordsAmount))
    myFile.close()

def main():
    global medianFile
    global lineWordsAmount
    lineWordsAmount = []
    INPUT_DIR = sys.argv[1]
    OUTPUT_PATH = sys.argv[2]
    medianFile = open(OUTPUT_PATH,'w')        # Median File updates in real time with the assumption that it is used like a log.
    directoryList = [f for f in listdir(INPUT_DIR) if isfile(join(INPUT_DIR,f)) ]   #for each file in the directory
    for f in sorted(directoryList):
        calcMedian(join(INPUT_DIR,f))  
    medianFile.close()

if __name__ == '__main__':
    main()