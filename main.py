# This is a sample Python script.
import sys

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.

from LineContentProcessor import process_file

if __name__ == '__main__':
    # Define variables
    textFileName = "sampleFile1.txt"  # placeholder example for file name
    systemArguments = sys.argv

    # allows file name to be selected from command line.
    if len(systemArguments) > 1:
        for fileName in systemArguments[1:]:
            process_file(fileName)
    else:
        process_file(textFileName)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
