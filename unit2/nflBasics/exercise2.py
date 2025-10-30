



def AddItUpMachine():
    print("please enter a number")
    number = input()
    values = []
    calculate = '7'
    while number =='7':
        values.append(number)
        print(values)
        print("please enter a number")
        number = input()

AddItUpMachine()

#################################################

def AddItUpMachine():
    print("please enter a number. Please enter 'q' to calculate")
    number = input()
    values = []
    while number != 'stop': #while whatever we type in IS NOT 0 do this...
        values.append(number)
        print(values)
        print("please enter a number")
        number = input()
    else:
        print('doing calculation..')
        total = sum(values)
        print(total)
        

pdCheck()

# Create a new python document caled  exercise3.py . Using th individual player helper function, 
# answer the following questions:
 

# NOTE = you will need to pass the position, year and week in as an agrument
# position example : quarterback = 'QB', runnerback = 'RB'

#weeklyPlayerStats('QB',2025,1) 

# 1. Who are the top 5 quarterbacks by passing yards? What’s their average completion percentage (cmp_pct)?

# 2. What might a high cmp_pct tell you about a quarterback’s style of play?