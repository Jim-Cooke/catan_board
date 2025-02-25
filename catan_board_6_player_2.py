# Program to generate balanced Catan boards for 6 player version

#  need to change due to there being 3 discs of the same number

# import libraries
import random
import time
import math
import array

#board - position 0 to 18
#      00  01  02
#    03  04  05  06
#  07  08  09  10  11
#12  13  14  15  16  17
#  18  19  20  21  22
#    23  24  25  26
#      27  28  29

#terrain type of tile and tile number
tile_ter = ['x']
tile_number = [0]
for n in range(1, 30):
    tile_ter.append('x')
    tile_number.append(0)
# terrain types: 2 desert, 6 field, 6 pasture, 6 forest, 5 hill, 5 mountain

# tiles next to each other
adj = [[1, 3, 4],  #00
           [0, 2, 4, 5],  #01
           [1, 5, 6],  #02
           [0, 4, 7, 8],  #03
           [0, 1, 3, 5, 8, 9],  #04
           [1, 2, 4, 6, 9, 10],  #05
           [2, 5, 10, 11],  #06
           [3, 8, 12, 13],  #07
           [3, 4, 7, 9, 13, 14],  #08
           [4, 5, 8, 10, 14, 15],  #09
           [5, 6, 9, 11, 15, 16],  #10
           [6, 10, 16, 17],  #11
           [7, 13, 18],  #12
           [7, 8, 12, 14, 18, 19],  #13
           [8, 9, 13, 15, 19, 20],  #14
           [9, 10, 14, 16, 20, 21],  #15
           [10, 11, 15, 17, 21, 22],  #16
           [11, 16, 22],  #17
           [12, 13, 19, 23],  #18
           [13, 14, 18, 20, 23, 24],   #19
           [14, 15, 19, 21, 24, 25],  #20
           [15, 16, 20, 22, 25, 26],  #21
           [16, 17, 21, 26],  #22
           [18, 19, 24, 27],  #23
           [19, 20, 23, 25, 27, 28],  #24
           [20, 21, 24, 26, 28, 29],  #25
           [21, 22, 25, 29],  #26
           [23, 24, 28],  #27
           [24, 25, 27, 29],  #28
           [25, 26, 28]]  #29

    

# list of terrain tiles 0 to 29
ter = ['desert',
           'desert',
           'field',
           'field',
           'field',
           'field',
           'field',
           'field',
           'pasture',
           'pasture',
           'pasture',
           'pasture',
           'pasture',
           'pasture',
           'forest',
           'forest',
           'forest',
           'forest',
           'forest',
           'forest',
           'hill',
           'hill',
           'hill',
           'hill',
           'hill',
           'mountain',
           'mountain',
           'mountain',
           'mountain',
           'mountain']

terrain = ['field', 'pasture', 'forest', 'hill', 'mountain']
# probability point for each terrain
prob_ter = {
    "field": 0,
    "pasture": 0,
    "forest": 0,
    "hill": 0,
    "mountain": 0
}
# red numbers on each terrain
red_ter = {
    "field": 0,
    "pasture": 0,
    "forest": 0,
    "hill": 0,
    "mountain": 0
}
# number discs - position 0 to 27
disc_number = [2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12]

#my random function
def random_1 ():
    r = random.random()
    t = time.time()
    # print(r, " ", t)
    rs = r + t
    # print(rs)
    rs = rs - math.floor(rs)
    return rs


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
            p = int(30 * random_1())
            # print(p)
            # find unused tile location
            if tile_ter[p] == 'x':
                break
        # check that location p's terrain is not same as adjacent
        adjacent = 'no'
        for a1 in adj[p]:
            if tile_ter[a1] == n:
                # adjacent to same thing
                # print('adj')
                adjacent = 'yes'
                # make 30 attempts to find a good tile
                for att in range(0, 30):
                    p = int(30 * random_1())
                    # print(p)
                    if tile_ter[p] == 'x':
                        # print('found unused')
                        adjacent = 'no'
                        for a2 in adj[p]:
                            if tile_ter[a2] == n:
                                # print('adj')
                                adjacent = 'yes'
                                break
                        if adjacent == 'no':
                            # found a good tile, break out of 30-for loop
                            break
                # failed to find a good tile 
                if adjacent == 'yes':
                    f1 = f1 + 1
                    print(f1)
                    break
        if adjacent == 'yes':
            # reset everything, start over
            for reset in range(0, 30):
                tile_ter[reset] = 'x'
            break
        # not same as adjacent, so set the tile
        tile_ter[p] = n
        # print(tile_ter[p])
        # repeat loop with new n
    # if loop finished break out
    if adjacent == 'no':
        break
  
# board of terrain tiles complete
print('tiles complete')
# print(tile_ter)


#print errors
print ('number of arrangements of hexagons', f1)


print('                  ', tile_ter[0], '  ', tile_ter[1], '  ', tile_ter[2])
print('            ', tile_ter[3], '  ', tile_ter[4], '  ', tile_ter[5], '  ', tile_ter[6])
print('      ', tile_ter[7], '  ', tile_ter[8], '  ', tile_ter[9], '  ', tile_ter[10], '  ', tile_ter[11])
print(tile_ter[12], '  ', tile_ter[13], '  ', tile_ter[14], '  ', tile_ter[15], '  ', tile_ter[16], '  ', tile_ter[17])
print('      ', tile_ter[18], '  ', tile_ter[19], '  ', tile_ter[20], '  ', tile_ter[21], '  ', tile_ter[22])
print('            ', tile_ter[23], '  ', tile_ter[24], '  ', tile_ter[25], '  ', tile_ter[26])
print('                  ', tile_ter[27], '  ', tile_ter[28], '  ', tile_ter[29])

# place number disks
# rules
# red (6 and 8) cannot be adjacent
# same number disks cannot be adjacent
# same number disks cannot be on same terrain type
# red disks cannot be adjacent to a 5 and 9 which are adjacent to each other
# each terrain type must have a red disk
# terrain types to be less that 1.5 times more probability points than each other

# add number discs to board
# various rules
f2 = 0
while True:
    # go through number tokens
    # previous disc number
    prev = 0
    prev_prev = 0
    # previous location
    prev_p = 99
    prev_prev_p = 99
    for nt in disc_number:
        # print(nt)
        status = 'good'
        # find location
        # generate location, test it.
        # only start over if 30 locations fail
        for att in range(0, 30):
            status = 'good'
            while True:
                # p is location
                p = int(30 * random_1())
                # find unused tile location, not desert
                # print(p)
                if tile_ter[p] != 'desert' and tile_number[p] == 0:
                    break
            # red (6 and 8) cannot be adjacent
            if (nt==6 or nt==8) and (prev==6 or prev==8):
                # test for adjacency
                for a in adj[p]:
                    if (tile_number[a]==6 or tile_number[a]==8):
                        status = 'bad'
                        f2 = f2 + 1
                        print(f2, ' red disk adjacent')
                        continue
            # same number disks cannot be adjacent
            # same numbered discs are adjacent for prev
            if nt == prev:
                for a in adj[p]:
                    if a == prev_p:
                        status = 'bad'
                        f2 = f2 + 1
                        print(f2, ' equal disc adjacent')
                        break
                if status == 'bad':
                    continue
            # same numbered discs are adjacent for previous to previous
            if nt == prev_prev:
                for a in adj[p]:
                    if a == prev_prev_p:
                        status = 'bad'
                        f2 = f2 + 1
                        print(f2, ' equal disc adjacent')
                        break
                if status == 'bad':
                    continue
            # same number disks cannot be on same terrain type
            # previous
            if nt == prev:
                if tile_ter[p] == tile_ter[prev_p]:
                     status = 'bad'
                     f2 = f2 + 1
                     print(f2, ' equal disc on same terrain')
                     continue
            # previous to previous
            if nt == prev_prev:
                if tile_ter[p] == tile_ter[prev_prev_p]:
                     status = 'bad'
                     f2 = f2 + 1
                     print(f2, ' equal disc on same terrain')
                     continue
            # red disks cannot be adjacent to a 5 and 9 which are adjacent to each other
            if nt == 9:
                # find adjacent 5
                for a3 in adj[p]:
                    if tile_number[a3] == 5:
                        # find adjacent 6 or 8
                        for b3 in adj[a3]:
                            if tile_number[b3] == 6 or tile_number[b3] == 8:
                                # see if it is adjacent to p
                                for c3 in adj[b3]:
                                    if c3 == p:
                                        status = 'bad'
                                        f2 = f2 +1
                                        print(f2, 'too-powerful triple')
                                        break
                            if status == 'bad':
                                break
                    if status == 'bad':
                        break
                if status == 'bad':
                    continue
            # each terrain type must have a red disk
            if nt == 6 or nt == 8:
                if red_ter[tile_ter[p]] > 1:
                    status = 'bad'
                    f2 = f2 +1
                    print(f2, 'red disk terrain imbalance')
                    continue
                for r3 in terrain:
                    if red_ter[r3] > 1 and red_ter[tile_ter[p]] > 0:
                        status = 'bad'
                        f2 = f2 +1
                        print(f2, 'red disk terrain imbalance')
                        break
                if status == 'bad':
                    continue                   
                        
            # it survives tests
            if status == 'good':
                break
        if status == 'bad':
            # reset everything, break out of for loop
            for n in range(0, 30):
                tile_number[n] = 0
            for tt in terrain:
                prob_ter[tt] = 0
                red_ter[tt] = 0
            break
        # disc is ok
        print(nt)
        # add to count of red disks on different terrain
        if nt == 6 or nt == 8:
            red_ter[tile_ter[p]] = red_ter[tile_ter[p]] + 1
        # find out probability
        if nt == 2 or nt == 12:
            dots = 1
        if nt == 3 or nt == 11:
            dots = 2
        if nt == 4 or nt == 10:
            dots = 3
        if nt == 5 or nt == 9:
            dots = 4
        if nt == 6 or nt == 8:
            dots = 5
        prob_ter[tile_ter[p]] = prob_ter[tile_ter[p]] + dots
        tile_number[p] = nt
        # previous and previous to previous locations and discs saved
        prev_prev = prev
        prev = nt
        prev_prev_p = prev_p
        prev_p = p
        # repeat loop with new nt
    # if loop finished break out
    if status == 'good':
        break
            
#print errors
print ('number of arrangements of hexagons', f1)
print ('number of arrangements of discs', f2)
# print (highp, ' ', lowp)

print('                  ', tile_ter[0], tile_number[0], '  ', tile_ter[1], tile_number[1], '  ', tile_ter[2], tile_number[2])
print('            ', tile_ter[3], tile_number[3], '  ', tile_ter[4], tile_number[4], '  ', tile_ter[5], tile_number[5], '  ', tile_ter[6], tile_number[6])
print('      ', tile_ter[7], tile_number[7], '  ', tile_ter[8], tile_number[8], '  ', tile_ter[9], tile_number[9], '  ', tile_ter[10], tile_number[10], '  ', tile_ter[11], tile_number[11])
print(tile_ter[12], tile_number[12], '  ', tile_ter[13], tile_number[13], '  ', tile_ter[14], tile_number[14], '  ', tile_ter[15], tile_number[15], '  ', tile_ter[16], tile_number[16], '  ', tile_ter[17], tile_number[17])
print('      ', tile_ter[18], tile_number[18], '  ', tile_ter[19], tile_number[19], '  ', tile_ter[20], tile_number[20], '  ', tile_ter[21], tile_number[21], '  ', tile_ter[22], tile_number[22])
print('            ', tile_ter[23], tile_number[23], '  ', tile_ter[24], tile_number[24], '  ', tile_ter[25], tile_number[25], '  ', tile_ter[26], tile_number[26])
print('                  ', tile_ter[27], tile_number[27], '  ', tile_ter[28], tile_number[28], '  ', tile_ter[29], tile_number[29])





