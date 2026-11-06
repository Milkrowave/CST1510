"""
RECORD CHECK  -  my version
===========================

Name  : Mikael Hisaindee
Lane  : Cyber      (delete two)
Date  : 06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Parses and cleans one raw messy line into a dictionary and handles inconsistent spacing and cases"""
    raw_line = raw_line.strip()
    SRC,rest = raw_line.split(",", 1) 
    SRC = SRC.strip()
    rest = rest.split(",")
    result = {"SRC": SRC}
    for i in range(len(rest)):
        key,value = rest[i].split("=")
        key = key.strip().upper()
        value = value.strip()
        if key != "RESULT":
            result[key] = float(value)
        else:
            value = value.upper()
            result[key] = value
    return result


def status_of(record):
    """returns the status of the record depending on its result"""
    if record["RESULT"] == "FAILED":
        return "FLAGGED"
    else:
        return "OK"
# ====================================================================== INPUT

raw_records = [] # initial empty list of raw records
with open("./LAB/RawRecords.txt", "r") as f: # opens the file in read mode
    for line in f:
        raw_records.append(line) # stores the lines read from the file into the list

# =============================================================== PROCESS + OUTPUT

RecordsCount,FlaggedCount = 0,0 # initialisation of data counters at 0
for raw_record in raw_records:
    RecordsCount += 1 # increments the records count at every instance on the iteration occuring
    CleanRecord = parse_line(raw_record)
    print(CleanRecord, " ", status_of(CleanRecord)) # outputs each clean record along with the return value of the status_of call
    if status_of(CleanRecord) == "FLAGGED":
        FlaggedCount += 1 # increments the flagged count depending on the condition being true or not
print("")
print(f"Total records{" ":>9}: {RecordsCount}")
print(f"Total records flagged : {FlaggedCount}")

# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [no error because no calculation is made in this lane] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
