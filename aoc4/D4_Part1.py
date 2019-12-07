a, b = 265275, 781584
# a, b = 112, 222
combos = [num for num in range(a, b)]
temp = []


def filter_combos(combos):
    for num in combos:
        if conditionals(num):
            temp.append(num)
    return len(temp)


def conditionals(num):
    '''
    checks for double
    then checks current digit > prev digit
    if all pass, then increment
    '''
    str_num = str(num)
    prevDigit = str_num[0]
    double = False

    for i in range(len(str_num)-1):
        if str_num[i+1] == prevDigit:
            double = True
        elif str_num[i+1] < prevDigit:
            return False
        else:
            prevDigit = str_num[i+1]

    return double
    

if __name__ == "__main__":
    print(filter_combos(combos))
    # print(conditionals(123456))
    # print(conditionals(112234))
    # print(conditionals(110012))
    # print(conditionals(123789))