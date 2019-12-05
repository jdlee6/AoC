a, b = 265275, 781574
# a, b = 112, 222

combos = [num for num in range(a, b)]

def filter_combos(combos):
    ''' 
    1. find adjacent digits (2 or more)
    2. find equal or increasing digits from L TO R
    3. append to list and return len of list
    '''
    temp = []
    for num in combos:
        if str(num)[0] == str(num)[1] or str(num)[1] == str(num)[2] or str(num)[2] == str(num)[3] or str(num)[3] == str(num)[4] or str(num)[4] == str(num)[5]:
            if str(num)[1] >= str(num)[0] and str(num)[2] >= str(num)[1] and str(num)[3] >= str(num)[2] and str(num)[4] >= str(num)[3] and str(num)[5] >= str(num)[4]:
                temp.append(num)

    return len(temp)


if __name__ == "__main__":
    print(filter_combos(combos))