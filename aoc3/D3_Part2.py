# dir1 = ['R8', 'U5', 'L5','D3']
# dir2 = ['U7', 'R6', 'D4', 'L4']
# (yes)

# dir1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# dir2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
# (yes)


# dir1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
# dir2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
# (yes)


def read_file(f):
    with open(f, 'r') as f:
        lines = f.readlines()

        dir1 = lines[0].split(',')
        dir1 = [i.strip() for i in dir1]
        # print(dir1)

        dir2 = lines[1].split(',')
        dir2 = [i.strip() for i in dir2]
        # print(dir2)

    return dir1, dir2

def find_coords(direc):
    ''' find every single coordinate and stores in a set ''' 
    x, y = 0, 0
    temp = set()
    
    for pair in direc:
        if pair[0] == 'R':
            for _ in range(int(pair[1:])):
                x += 1
                # print(x,y)
                temp.add((x, y))

        elif pair[0] == 'U':
            for _ in range(int(pair[1:])):
                y += 1
                # print(x,y)
                temp.add((x, y))

        elif pair[0] == 'L':
            for _ in range(int(pair[1:])):
                x -= 1
                # print(x,y)
                temp.add((x, y))

        elif pair[0] == 'D':
            for _ in range(int(pair[1:])):
                y -= 1
                # print(x,y)
                temp.add((x, y))

    return temp


def find_intersections(a, b):
    ''' takes 2 sets and finds intersection '''
    return a.intersection(b)


def find_steps(a, b, direction):
    '''
    walk through individual coords
    for every coord += step
    repeat the process for the next intersection 
    return that array
    '''

    steps = []
    d = dict()

    for intersection in find_intersections(a, b):
        u, z = intersection[0], intersection[1]
        step = 0
        x, y = 0, 0

        for pair in direction:
            if pair[0] == 'R':
                for _ in range(int(pair[1:])):
                    x += 1 
                    step += 1
                    if (x,y) == (u,z):
                        steps.append(step)
                        break

            elif pair[0] == 'U':
                for _ in range(int(pair[1:])):
                    y += 1
                    step += 1
                    if (x,y) == (u,z):
                        steps.append(step)
                        break

            elif pair[0] == 'L':
                for _ in range(int(pair[1:])):
                    x -= 1
                    step += 1
                    if (x,y) == (u,z):
                        steps.append(step)
                        break

            elif pair[0] == 'D':
                for _ in range(int(pair[1:])):
                    y -= 1
                    step += 1
                    if (x,y) == (u,z):
                        steps.append(step)
                        break

    return steps


if __name__ == "__main__":
    dir1, dir2 = read_file('./input.txt')

    a = find_steps(find_coords(dir1), find_coords(dir2), dir1)
    b = find_steps(find_coords(dir1), find_coords(dir2), dir2)
    
    # print(a, b)
    print(min([sum(x) for x in list(zip(a,b))]))