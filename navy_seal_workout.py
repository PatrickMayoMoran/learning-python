import json

"""To Do:
-write in data with associated date or just order
-check to see if data point is a new record for time, total, or per min
-congratulate user for any records set
-explain the workout this program is for
-identify and print historical bests in total time and per min
-print how many days in a row workout has been done
-write in/read out data correctly
"""

def main():
    greet_user()
    minutes, flutter, push = get_stats()

def greet_user():
    #Greet the User with a simple greeting
    print("""Wazzup boi!
    \rHope the workout was good.
    \rLet's see how you did.\n""")

def get_stats():
    #Get the input for the three main data points from the workout
    minutes = float(input("How many minutes did you work out? "))
    flutter = float(input("How many minutes of flutter? "))
    push = float(input("How many pushups? "))
    push_per_min = "{:.2f}".format(push / minutes)
    flutter_per_min = "{:.2f}".format(flutter / minutes * 60)
    print(f"""
    \rSo in {minutes} minutes, you did {flutter} minutes of flutter
    \rand {push} pushups.\n
    \rThat works out to {push_per_min} pushups per minute,
    \rand {flutter_per_min} seconds of flutter per minute.\n""")

    return minutes, flutter, push

if __name__ == '__main__':
    main()
