"""
This file is meant to process the content of a MedPC output text file.
"""

MAX_LINES_IN_INPUT = 7500


def process_line_content(line: str) -> list:
    """
    This function processes the content of a line and reformat it as a list of strings
    :param line: the content of the line
    :return: a list of strings
    """
    return line.strip().split()[1:]


def read_until_target_inline(target, infile):
    line = ""
    iteration = 0
    while target not in line and iteration < MAX_LINES_IN_INPUT:
        line = infile.readline()
        iteration += 1
    return line


def check_for_expected_term(expected_term, line, infile):
    if expected_term not in line:
        print(f"{infile} did not have the correct format\nMissing {expected_term}")
        return False
    return True


def get_output_filename(infile, file_name):
    # get the start date
    line = read_until_target_inline("Start Date", infile)
    if not (check_for_expected_term("Start Date", line, file_name) and len(line.split(":")) > 1):
        return
    date = line.split(":")[1].strip().replace("/", "_")

    # get box used
    line = read_until_target_inline("Box", infile)
    if not check_for_expected_term("Box", line, file_name):
        return
    boxId = line.strip().replace(": ", "_")

    # get start time
    line = read_until_target_inline("Start Time", infile)
    if not (check_for_expected_term("Start Time", line, file_name) and len(line.split(":")) > 1):
        return
    startTime = line.strip().split(": ")[1].split(":")
    startTime = startTime[0] + "h" + startTime[1] + "m"

    return "_".join([date, boxId, startTime]) + ".csv"


def process_file(textFileName: str):
    """
    This function processes the content of a file and reformat it as a list of strings
    :param textFileName: the name of the file
    """
    # Open the file for reading
    infile = open(textFileName, "r")
    line = ""
    defTime = 0
    eventLog = {defTime: []}
    eId = "100"

    csvFileName = get_output_filename(infile, textFileName)
    if csvFileName is None:
        return

    while "C:" not in line.strip():
        line = infile.readline()
    # Process the rest of the file
    while eId != "300":
        line = infile.readline()
        if len(line.strip()) <= 2:  # handles edge case where end code is never written out
            break
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
        for tEvent in eventLog[timeVal]:
            outfile.write(f"{timeVal},{tEvent}\n")
    outfile.close()
