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
    csvFileName = textFileName.strip().split(".")[0] + ".csv"
    line = ""

    while ("Start Date" not in line):
        line = infile.readline()

    date = line.split(":")[1].strip().replace("/", "_")

    while("Box" not in line):
        line = infile.readline()
    
    boxId = line.strip().replace(": ", "_")       

    while ("Start Time" not in line):
        line = infile.readline()

    startTime = line.strip().split(": ")[1].split(":")
    startTime = startTime[0] + "h" + startTime[1] + "m"
    
    while(line.strip() != "C:"):
        line = infile.readline()

    csvFileName = "_".join([date, boxId, startTime]) + ".csv"

    defTime = 0
    eventLog = {}
    eventLog[defTime] = []
    eId = "100"
    # Process the rest of the file
    while (eId != "300"):
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
