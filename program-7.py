import sys
import math

if len(sys.argv) == 4:
    English = int(sys.argv[1])
    Maths = int(sys.argv[2])
    Science = int(sys.argv[3])
    print("User input provided")
else:
    English = 96
    Maths = 80
    Science = 91

scores = [English, Maths, Science]

total = sum(scores)
avg = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("---- Results ----")
print(f"English : {English}, Maths : {Maths}, Science : {Science}")
print(f"Total : {total}")
print(f"Average : {avg:.2f}")
print(f"Maximum Score : {maximum}")
print(f"Minimum Score : {minimum}")