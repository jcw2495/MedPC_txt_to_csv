"""
This file is meant to process the content of a line and reformat it as a list of strings
"""


def process_line_content(line: str) -> list:
    """
    This function processes the content of a line and reformat it as a list of strings
    :param line: the content of the line
    :return: a list of strings
    """
    lineContent = []
    line = line.strip()
    lineList = line.split()
    for word in lineList:
        lineContent.append(word.strip())
    return lineContent


def process_file(textFileName: str):
    """
    This function processes the content of a file and reformat it as a list of strings
    :param textFileName: the name of the file
    """
    # Define variables
    textFileId = textFileName.split(".")[0]
    csvFileName = textFileId + ".csv"
    fileContent = []

    # Open the file for reading
    infile = open(textFileName, "r")

    # Discard header used (used for test file you sent me)
    for i in range(39):
        infile.readline()

    # Process the C table header
    line = infile.readline()
    line = [line[0], "0", "1", "2", "3", "4"]
    fileContent.append(line)

    # Process the rest of the file
    for i in range(121):
        line = infile.readline()
        lineContent = process_line_content(line)
        lineContent[0] = lineContent[0].replace(":", "")
        fileContent.append(lineContent)
    infile.close()

    outfile = open(csvFileName, "w")
    for line in fileContent:
        csvLine = ",".join(line) + "\n"
        outfile.write(csvLine)
    outfile.close()