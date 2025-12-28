import sys
if len (sys.argv) == 4 :
    script_name = sys.argv[0]
    principle = sys.argv[1]
    rate = sys.argv[2]
    time = sys.argv[3]
else :
    script_name = sys.argv[0]
    principle = 1000.0
    rate = 5-0
    time = 2-0
    simple_interest = (principle * rate * time ) / 100.0
    print (f"Simple interest = {simple_interest :.2f}")

    print (f"The Principle = {principle}")
    print(f"The Rate Of Interest : {rate}")
    print(f"The time : {time}")
    