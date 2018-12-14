def calcstep(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']

    sum = 0
    for i in range(begin,end+1,step):
        sum += i

    return sum

print("3~5 = ", calcstep(begin=3,end=5,step=1))


