lottery = [43, 21, 99, 18, 37, 99]
with open('lottery.dat', 'w') as f:
    for number in lottery:
        f.write(str(number) +'\n')