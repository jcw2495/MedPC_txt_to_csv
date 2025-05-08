import sys

from FileProcessor import process_file

if __name__ == '__main__':
    # placeholder example for file name
    textFileName = "sampleFile1.txt"

    # allows file name/names to be selected from command line
    if len(sys.argv) > 1:
        for fileName in sys.argv[1:]:
            process_file(fileName)
    else:
        process_file(textFileName)