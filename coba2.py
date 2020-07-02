def displayPathtoPrincess(n,grid):
    # pairing element with its index
    partner = zip([x for row in grid for x in row], [(i, j) for i in range(n) for j in range(n)])

    # get index of m
    m = list((data[1] for data in partner if data[0] == 'm'))[0]
    # get index of p
    p = list((data[1] for data in partner if data[0] == 'p'))[0]

    horizontal = m[0] - p[0]
    vertical = m[1] - p[1]

    if horizontal > 0:
        print('RIGHT' * horizontal)
    else:
        print('LEFT' * abs(horizontal))

    if vertical > 0:
        print('DOWN' * vertical)
    else:
        print('UP' * abs(vertical))
    


print(displayPathtoPrincess(4, ['----', '--m-', 'p---', '----']))