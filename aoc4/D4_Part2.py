a, b = 265275, 781584
combos = [num for num in range(a, b)]
res = []


def filter_combos(combos):
    for num in combos:
        if conditionals(num):
            checkForPair(num)

    return len(res)
    

def checkForPair(num):
    '''
    if digit count == 2
    appends to results then break
    '''
    num = str(num)
    for digit in num:
        count = num.count(digit)
        # print(digit, count)
        if count == 2:
            res.append(num)
            break


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
    # checkForPair(1122333)
    # checkForPair(112233)
    # checkForPair(111122)
    # checkForPair(123444)
    # print(len(res))