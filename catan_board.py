# Program to generate balanced Catan boards
# import libraries
import random
import time
import math
import array

#board - position 0 to 18
#  A B C
# D E F G
#H I J K L
# M N O P
#  Q R S

tile_label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
tile_ter = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
# terrain types: 1 desert, 4 field, 4 pasture, 4 forest, 3 hill, 3 mountain
tile_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# tiles next to each other
adj = [[1, 3, 4],  #A
           [0, 2, 4, 5],  #B
           [1, 5, 6],  #C
           [0, 4, 7, 8],  #D
           [0, 1, 3, 5, 8, 9],  #E
           [1, 2, 4, 6, 9, 10],  #F
           [2, 5, 10, 11],  #G
           [3, 8, 12],  #H
           [3, 4, 7, 9, 12, 13],  #I
           [4, 5, 8, 10, 13, 14],  #J
           [5, 6, 9, 11, 14, 15],  #K
           [6, 10, 15],  #L
           [7, 8, 13, 16],  #M
           [8, 9, 12, 14, 16, 17],  #N
           [9, 10, 13, 15, 17, 18],  #O
           [10, 11, 14, 18],  #P
           [12, 13, 17],  #Q
           [13, 14, 16, 18],  #R
           [14, 15, 17]]  #S

terrain = ['field', 'pasture', 'forest', 'hill', 'mountain']
fives = ['x', 'x']
nines = ['x', 'x']
# list of terrain tiles 0 to 18
ter = ['desert',
           'field',
           'field',
           'field',
           'field',
           'pasture',
           'pasture',
           'pasture',
           'pasture',
           'forest',
           'forest',
           'forest',
           'forest',
           'hill',
           'hill',
           'hill',
           'mountain',
           'mountain',
           'mountain']

# number discs - position 0 to 17
disc_number = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

#my random function
def random_1 ():
    r = random.random()
    t = time.time()
    # print(r, " ", t)
    rs = r + t
    # print(rs)
    rs = rs - math.floor(rs)
    return rs

# function to count x in terrain
def nox_ter(terrain):
    nox = 0
    for nn in range(0, 5):
        if terrain[nn] == 'x':
            nox = nox + 1
    return nox        

# create board with terrain tiles
# tiles of the same terrain should not be adjacent

# select terrain tiles in order
# pick random location
# if tile already there pick new location
# if new tile adjacent to one of same terrain
    # reset board, start again
f1 = 0    
while True:
    # go through terrain tiles
    for n in ter:
        # print(n)
        while True:
            # p is location
            p = int(19 * random_1())
            # find unused tile location
            if tile_ter[p] == 'x':
                break
        # check that location p's terrain is not same as adjacent
        adjacent = 'no'
        for a in adj[p]:
            if tile_ter[a] == n:
                # adjacent to same thing
                adjacent = 'yes'
                f1 = f1 + 1
                print(f1)
                break
        if adjacent == 'yes':
            # reset everything, start over
            tile_ter = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
            break
        # not same as adjacent, so set the tile
        tile_ter[p] = n
        # repeat loop with new n
    # if loop finished break out
    if adjacent == 'no':
        break
  
# board of terrain tilse complete

# add number discs to board
# various rules
f2 = 0
while True:
    # go through number tokens
    # previous disc number
    prev = 0
    # previous location
    prev_p = 0 
    for nt in disc_number:
        # print(nt)
        status = 'good'
        # find location
        while True:
            # p is location
            p = int(19 * random_1())
            # find unused tile location, not desert
            # print(p)
            if tile_ter[p] != 'desert' and tile_number[p] == 0:
                break
        # location is not desert and does not already have a number
        #while loop around tests
        while True:
            # if 6 or 8 cannot be adjacent to 6 or 8
            if (nt==6 or nt==8) and (prev==6 or prev==8):
                # test for adjacency
                for a in adj[p]:
                    if (tile_number[a]==6 or tile_number[a]==8):
                        status = 'bad'
                        f2 = f2 + 1
                        print(f2, ' red disk adjacent')
                        break
            if status == 'bad':
                break
            # test for same numbered discs
            if nt == prev:
                # same numbered discs on same terrain
                if tile_ter[p] == tile_ter[prev_p]:
                    status = 'bad'
                    f2 = f2 + 1
                    print(f2, ' equal disc on same terrain')
                    break
                # same numbered discs are adjacent
                for a in adj[p]:
                    if a == prev_p:
                        status = 'bad'
                        f2 = f2 + 1
                        print(f2, ' equal disc adjacent')
                        break
                if status == 'bad':
                    break
            # record terrain type of fives
            if nt == 5 and prev != 5:
                fives[0] = tile_ter[p]
            if nt == 5 and prev == 5:
                fives[1] = tile_ter[p]
            # test for 6, 8 on four different terrain types
            if nt == 6 or nt == 8:
                for tt in range(0, 5):
                    if tile_ter[p] == terrain[tt]:
                        terrain[tt] = 'x'
                        break
                if nt == 6 and prev == 6 and nox_ter(terrain) != 2:
                    status = 'bad'
                    f2 = f2 + 1
                    print(f2, '6 or 8 on same terrain')
                    break
                if nt == 8 and prev == 6 and nox_ter(terrain) != 3:
                    status = 'bad'
                    f2 = f2 + 1
                    print(f2, '6 or 8 on same terrain')
                    break
                if nt == 8 and prev == 8 and nox_ter(terrain) != 4:
                    status = 'bad'
                    f2 = f2 + 1
                    print(f2, '6 or 8 on same terrain')
                    break
            # find terrain without 6 or 8
            if nt == 9 and prev == 9:    
                for t68 in range(0, 5):
                    if terrain[t68] != 'x':
                        not68ter = terrain[t68]
                        break
            # record terrain type of nines
            if nt == 9 and prev != 9:
                nines[0] = tile_ter[p]
            if nt == 9 and prev == 9:
                nines[1] = tile_ter[p]
            # a 5 and a 9 must be on the terrain that has no 6 or 8
            if (nt == 9 and prev == 9) and ((fives[0] != not68ter and fives[1] != not68ter) or (nines[0] != not68ter and nines[1] != not68ter)):
                status = 'bad'
                f2 = f2 + 1
                print(f2, 'terrain without 6 or 8 does not have 5 and 9')
            # mountains should have a 5 or 9
            if (nt == 9 and prev == 9) and (fives[0] != 'mountain' and fives[1] != 'mountain' and nines[0] != 'mountain' and nines[1] != 'mountain'):
                status = 'bad'
                f2 = f2 +1
                print(f2, 'mountain has no 5 or 9')
            # hills should have a 5 or 9
            if (nt == 9 and prev == 9) and (fives[0] != 'hill' and fives[1] != 'hill' and nines[0] != 'hill' and nines[1] != 'hill'):
                status = 'bad'
                f2 = f2 +1
                print(f2, 'hill has no 5 or 9')
            # test for powerful triple
            if nt == 9:
                # find adjacent 5 or 6 or 8
                for a3 in adj[p]:
                    if tile_number[a3] == 6 or tile_number[a3] == 8 or tile_number[a3] == 5:
                        # find hexes adjacent to both of them
                        for m3 in adj[p]:
                            for n3 in adj[a3]:
                                if (m3 == n3) and (tile_number[n3] == 6 or tile_number[n3] == 8 or tile_number[n3] == 5):
                                    status = 'bad'
                                    f2 = f2 +1
                                    print(f2, 'too-powerful triple')
                                    break
                            if status == 'bad':
                                break
                    if status == 'bad':
                        break
            # it survives all tests
            if status == 'good':
                break
        if status == 'bad':
            # reset everything, break out of for loop
            tile_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            terrain = ['field', 'pasture', 'forest', 'hill', 'mountain']
            fives = ['x', 'x']
            nines = ['x', 'x']
            break
        # disc is ok
        tile_number[p] = nt
        prev = nt
        prev_p = p
        # repeat loop with new nt
    # if loop finished break out
    if status == 'good':
        break
# number discs are complete
                

 
# select number tokens in order
# pick random location
# if desert or if disc already there pick new location

# test if same-numbered discs are adjacent-done
# test if same-numbered discs are on same terrain-done
# test if 6 or 8 are adjacent-done
# test that 6s, 8s are on four different terrain-done
# test that the terrain without 6 or 8 has 5 and 9-done
# test that mountain and hill have 5 and 9-done
# test that there are no triples of red with 5 and 9


#print board
for n in range(0, 19):
    print(tile_ter[n], ' ', tile_number[n])


print('            ', tile_ter[0], tile_number[0], '  ', tile_ter[1], tile_number[1], '  ', tile_ter[2], tile_number[2])
print('      ', tile_ter[3], tile_number[3], '  ', tile_ter[4], tile_number[4], '  ', tile_ter[5], tile_number[5], '  ', tile_ter[6], tile_number[6])
print(tile_ter[7], tile_number[7], '  ', tile_ter[8], tile_number[8], '  ', tile_ter[9], tile_number[9], '  ', tile_ter[10], tile_number[10], '  ', tile_ter[11], tile_number[11])
print('      ', tile_ter[12], tile_number[12], '  ', tile_ter[13], tile_number[13], '  ', tile_ter[14], tile_number[14], '  ', tile_ter[15], tile_number[15])
print('            ', tile_ter[16], tile_number[16], '  ', tile_ter[17], tile_number[17], '  ', tile_ter[18], tile_number[18])




