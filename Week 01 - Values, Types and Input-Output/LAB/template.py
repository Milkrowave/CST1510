"""
RECORD CHECK  -  my version
===========================

Name  : Mikael Hisaindee
Lane  :  AI     (delete two)
Date  : 26 / 08 / 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
# ================================================================== INPUT
label = input("Please enter data set name: ")
first = float(input("Please enter rows loaded: "))
second = float(input("Please enter rows expected: "))
# ================================================================== PROCESS
difference = first - second
percent = (first / second * 100) 
# ================================================================== PROCESS
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Rows loaded    : {first:>10.2f}")
print(f"Rows expected  : {second:>10.2f}")
print(f"Difference     : {difference:>+10.2f}")
print(f"Percentage     : {percent:>10.2f}%")

print("=" * 34)