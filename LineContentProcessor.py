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
    lineList = line.split()[1:]
    for word in lineList:
        lineContent.append(word.strip())
    return lineContent


def process_file(textFileName: str):
    """
    This function processes the content of a file and reformat it as a list of strings
    :param textFileName: the name of the file
    """
    # Open the file for reading
    infile = open(textFileName, "r")

    for i in range(4):
        infile.readline()

    dateLine = infile.readline()
    date = dateLine.strip().split(":")[1]
    date = date.replace("/", "_")

    for i in range(4):
        infile.readline()

    boxLine = infile.readline()
    box = boxLine.strip().replace(": ", "")

    csvFileName = date + "_" + box + ".csv"

    # Discard header used (used for test file you sent me)
    for i in range(30):
        infile.readline()

    defTime = 0
    eventLog = {}
    eventLog[defTime] = []
    # Process the rest of the file
    for i in range(121):
        line = infile.readline()
        lineContent = process_line_content(line)
        for event in lineContent:
            eTime, eId = event.split(".")
            eTime = int(eTime)
            if eTime > 0:
                defTime += eTime
                eventLog[defTime] = []
            eventLog[defTime].append(eId)
    infile.close()

    # Write the event log to a CSV file
    outfile = open(csvFileName, "w")
    for timeVal in eventLog:
        csvLine = str(timeVal) + "," + ",".join(eventLog[timeVal]) + "\n"
        outfile.write(csvLine)
    outfile.close()
