"""
RECORD CHECK  -  my version
===========================

Name  :  Mikael Hisaindee
Lane  :  Cyber     (delete two)
Date  :  23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ====================================================================== CLASS


# your class goes here
class Record:
    over_limit_count = 0
    def __init__(self, label, value, limit):
        """initialises all attributes to the class object as passed"""
        self.label = label
        self.value = value
        self.limit = limit
        if Record.status(self) == "OVER LIMIT": # uses status method during the instance of creation of object
            Record.over_limit_count += 1
    def status(self):
        """this class method calculates a percentage and determines the status of the record"""
        percent = (self.value/self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS


def load_records(path):
    """reads a record file and splits the values into 3 dedicated variables. returns a list of the records"""
    ListOfRecords = [] # initial empty list
    with open(path, "r") as f:
        for file in f:
            line = file.strip()
            label,value,limit = line.split(",")
            value = int(value)
            limit = int(limit)
            ListOfRecords.append(Record(label,value,limit)) # list builds as the lines in file is read
    return ListOfRecords


# ==================================================================== OUTPUT


for record in load_records("LAB/Records.txt"):
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    print(f"Failed logins     : {record.value:>10.2f}")
    print(f"Total attemps     : {record.limit:>10.2f}")
    print(f"status            : {record.status():>10}") # uses status method 

    print("=" * 34)
print("Total records OVER LIMIT: ", Record.over_limit_count) # output of over limit counter through the class itself


# ==========================================================================

