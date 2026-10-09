"""
RECORD CHECK  -  srv-01
===========================

Name  : Mikael Hisaindee
Lane  :  IT      (delete two)
Date  : 08/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS



def status_of(percent):
    """returns status of the percentage"""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"
def check(value, limit):
    """calculates and returns the difference and the percentage as two values"""
    difference = limit - value
    percentage = (value/limit) * 100
    return difference, percentage
def print_report(label, value, limit, difference, percent, status):
    """prints all the data to the user"""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Used         : {value:>8.2f}")
    print(f"Total        : {limit:>8.2f}")
    print(f"Free         : {difference:>8.2f}")
    print(f"Percent      : {percent:>8.2f} %")
    print(f"Status       : {status:>8}")

    print("=" * 34)
count = 0
while True:
# ==================================================================== INPUT


    label = input("Please enter the label(enter quit to stop): ")
    if label == "quit":
        break
    value = float(input("Please enter GB used: "))    # replace with an input() call, converted
    limit = float(input("Please enter GB total: "))     # replace with an input() call, converted


# ================================================================== PROCESS


    difference, percentage = check(value, limit)    # replace with your code
     # replace with your code
    status = status_of(percentage)          # replace with your code
    if status == "OVER LIMIT":
        count += 1

# =================================================================== OUTPUT


    print_report(label, value, limit, difference, percentage, status)
print(f"Number of records OVER LIMIT: {count}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [division by 0 error] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
