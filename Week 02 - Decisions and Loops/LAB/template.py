"""
RECORD CHECK  -  srv-01
===========================

Name  :  Mikael Hisaindee
Lane  :  Cyber security    (delete two)
Date  :  02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
OverLimitCount = 0
while True : 
# ==================================================================== INPUT


    label = input("Please enter source IP (Enter 'quit' to stop): ")     
    if label == "quit":
        break
    value = float(input("Please enter failed logins: "))
    limit = float(input("Please enter total attemps: "))


# ================================================================== PROCESS


    difference = limit - value
    percent = value/limit * 100

    if percent >= 100:
        status = "OVER LIMIT"
        OverLimitCount += 1 
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

# =================================================================== OUTPUT


    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Failed logins  : {value:>10.2f}")
    print(f"Total attempts : {limit:>10.2f}")
    print(f"attempts left  : {difference:>10.2f}")
    print(f"Percent        : {percent:>10.2f}")
    print(f"status         : {status:>10}")

    print("=" * 34)

print("Number of records over limit: ", OverLimitCount)
