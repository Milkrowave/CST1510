"""
RECORD CHECK  -  my version
===========================

Name  : Mikael Hisaindee
Lane  :  AI      (delete two)
Date  : 16/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS


def check_record(value, limit): # defining check_record function
    """calculates and returns the difference, the percentage and the status as two values"""
    difference = limit - value
    percentage = (value/limit) * 100
    if percentage >= 100:
        status = "OVER LIMIT"
    elif percentage >= 90:
        status = "WARNING"
    else:
        status = "OK"
    
    return difference, percentage, status
def print_report(label, value, limit, difference, percent, status): # defining print_report function
    """prints all the data to the user"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Rows loaded    : {value:>8.2f}")
    print(f"Rows expected  : {limit:>8.2f}")
    print(f"Difference     : {difference:>+8.2f}")
    print(f"Percentage     : {percent:>8.2f}%")
    print(f"Status         : {status:>8}")

    print("=" * 34)
# ====================================================================== STORE


def load_records(path):
    """takes a file path and puts the file contents into a list of dictionaries and assigns keys to designated values and returns the list"""
    records = []  
    with open(path, "r") as f:
        for file in f:
            line = file.strip()
            label,value,limit = line.split(",") # text split into the variables
            records.append({"label": label , "value": float(value) , "limit": float(limit)}) # building the list of dictionaries
        return records
with open("LAB/label-status.txt", "w") as f:
    try:
        Records = load_records("LAB/data.txt") # load_records called
    except FileNotFoundError:
        print("This file does not exist.")
        Records = [] 
    for i in range(len(Records)):
    
        _,_,status = check_record(Records[i]["value"], Records[i]["limit"]) # _ is a throwaway variable
        f.write(f"{Records[i]["label"]}, {status}\n")
with open("LAB/label-status.txt", "r") as f:    
    print(f.read())
    
# =============================================================== PROCESS + OUTPUT

OverLimitCount = 0
for i in range(len(Records)):
    Difference,Percentage,Status = check_record(Records[i]["value"], Records[i]["limit"]) # check_record called
    print_report(Records[i]["label"], Records[i]["value"], Records[i]["limit"], Difference, Percentage, Status) # print_report called
    if Status == "OVER LIMIT":
        OverLimitCount += 1
print(OverLimitCount)
# ==========================================================================



#    [file not found error] If you are loading from a file, check what happens when the file
#        does not exist - write the error down

