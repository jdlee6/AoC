a, b = 265275, 781584
combos = [num for num in range(a, b)]
res = []


def filter_combos(combos):
    for num in combos:
        if str(num)[0] == str(num)[1] or str(num)[1] == str(num)[2] or str(num)[2] == str(num)[3] or str(num)[3] == str(num)[4] or str(num)[4] == str(num)[5]:
            if str(num)[1] >= str(num)[0] and str(num)[2] >= str(num)[1] and str(num)[3] >= str(num)[2] and str(num)[4] >= str(num)[3] and str(num)[5] >= str(num)[4]:
                filter_more(num)


def filter_more(num):
    '''
    if digit count == 2
    break
    '''
    num = str(num)
    for digit in num:
        count = num.count(digit)
        # print(digit, count)
        if count == 2:
            res.append(num)
            break


if __name__ == "__main__":
    filter_combos(combos)
    # filter_more(1122333)
    # filter_more(112233)
    # filter_more(111122)
    # filter_more(123444)
    print(len(res))































'''
    # # find unique digits
    # for d in str(num):
    #     if d 


    # iterate through each possible num
    # need to filter again 
    # stack
    stack = []

    for digit in str(num):
        print(stack)
        if digit not in stack:
            stack.append(digit)
        else:
            stack.pop()
    
    print(stack)
'''
