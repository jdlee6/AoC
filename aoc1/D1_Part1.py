temp = []

def find_fuel(mass):
    ''' find fuel for each mass '''
    fuel = (mass // 3) - 2
    return fuel

def read_file(f):
    ''' return a list of all the masses '''
    with open(f, 'r') as f:
        for line in f:
            mass = line.split()
            temp.append(int(''.join(mass)))
    # print(temp)
    return temp


def calc_fuel(array):
    ''' sum all of the calculated fuels '''
    realFuel = [find_fuel(mass) for mass in array]
    sumFuel = sum(realFuel)
    # print(sumFuel)
    return sumFuel


def main():
    read_file('./AoC1.txt')
    print(calc_fuel(temp))


if __name__ == "__main__":
    main()