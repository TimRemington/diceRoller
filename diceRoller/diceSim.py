# Dice Rolling Simulator - InterCon

import random

def Roll(rule, dieNumber):
    successes = 0
    # Rules for 10-again (standard roll)
    if rule == 10:
        for x in range (dieNumber):
            result = random.randint(1,10)
            if result > 7 and result < 10:
                successes = successes + 1
            elif result == 10:
                successes = successes + 1
                result = random.randint(1,10)
                if result > 7:
                    successes = successes + 1
    # Rules for 9-again
    elif rule == 9:
        for x in range (dieNumber):
            result = random.randint(1,10)
            if result == 8:
                successes = successes + 1
            elif result > 8:
                successes = successes + 1
                result = random.randint(1,10)
                if result > 7:
                    successes = successes + 1
    # Rules for 8-again
    elif rule == 8:
        for x in range (dieNumber):
            result = random.randint(1,10)
            if result > 7:
                successes = successes + 1
                result = random.randint(1,10)
                if result > 7:
                    successes = successes + 1
    # Rules for Force 1
    elif rule == 11:
        for x in range (dieNumber):
            result = random.randint(1,10)
            if result > 7 and result < 10:
                successes = successes + 1
            elif result == 10:
                successes = successes + 1
                result = random.randint(1,10)
                if result > 7:
                    successes = successes + 1
        if successes > 0:
            successes = successes + 1
    # Rules for Infinite Explosion 8-again
    elif rule == 1:
        dieCount = dieNumber
        while dieCount > 0:
            for x in range(dieCount):
                result = random.randint(1,10)
                if result > 7:
                    successes = successes + 1
                else:
                    dieCount = dieCount - 1


    return successes

def RunStats (trials, rule, dieNumber):
    successes = [0]*trials
    for x in range (trials):
        successes[x] = Roll(rule,dieNumber)
        avg = sum(successes)/len(successes)

    err = [0]*trials
    for y in range (trials):
        err[y] = (successes[y]-avg)**2

    std = (sum(err)/(len(successes) - 1))**0.5
    # if rule == 10:
    #     print("10-again: ", dieNumber, "dice rolled ", trials, "times:")
    # elif rule == 9:
    #     print("9-again: ", dieNumber, "dice rolled ", trials, "times:")
    # elif rule == 8:
    #     print("8-again: ", dieNumber, "dice rolled ", trials, "times:")
    # elif rule == 11:
    #     print("Force 1: ", dieNumber, "dice rolled ", trials, "times:")
    # elif rule == 1:
    #     print("Infinite Explosion 8-again: ", dieNumber, "dice rolled ", trials, "times:")
    # print("Average: ",avg)
    # print("Standard Deviation: ",std)

    return {"Successes": successes,"Trials": trials, "Again": rule, "Dice Number": dieNumber, "Average": avg,'Standard Deviation': std}


# Use the function runStats(number of trials, rule used, number of dice rolled)
# 10000 trials is a good rule of thumb
# runStats(10000, 10, 13)
# runStats(10000, 9, 19)
# runStats(10000, 8, 18)
# runStats(10000, 1, 18)
