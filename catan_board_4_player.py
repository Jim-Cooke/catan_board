# Program to generate balanced Catan boards for 4 player version
# using techniques developed in 6 player version

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
#    12  13  14  15
#      16  17  18  


#terrain type of tile and tile number
tile_ter = ['x']
tile_number = [0]
for n in range(1, 19):
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
           [3, 8, 12],  #07
           [3, 4, 7, 9, 12, 13],  #08
           [4, 5, 8, 10, 13, 14],  #09
           [5, 6, 9, 11, 14, 15],  #10
           [6, 10, 15],  #11
           [7, 8, 13, 16],  #12
           [8, 9, 12, 14, 16, 17],  #13
           [9, 10, 13, 15, 17, 18],  #14
           [10, 11, 14, 18],  #15
           [12, 13, 17],  #16
           [13, 14, 16, 18],  #17
           [14, 15, 17]]  #18

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
# number discs - position 0 to 18
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
                # make 19 attempts to find a good tile
                for att in range(0, 19):
                    p = int(19 * random_1())
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
            for reset in range(0, 19):
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
print('            ', tile_ter[12], '  ', tile_ter[13], '  ', tile_ter[14], '  ', tile_ter[15])
print('                  ', tile_ter[16], '  ', tile_ter[17], '  ', tile_ter[18])

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
        for att in range(0, 19):
            status = 'good'
            while True:
                # p is location
                p = int(19 * random_1())
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
            # same number disks cannot be on same terrain type
            # previous
            if nt == prev:
                if tile_ter[p] == tile_ter[prev_p]:
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
            # each terrain type must have at most one red disk
            if nt == 6 or nt == 8:
                if red_ter[tile_ter[p]] > 0:
                    status = 'bad'
                    f2 = f2 +1
                    print(f2, 'red disk terrain imbalance')
                    continue
            # test even probabilities of terrain types
            if nt == 12:
                high_p = 0
                low_p = 99
                for pt in terrain:
                    if prob_ter[pt] > high_p:
                        high_p = prob_ter[pt]
                    if prob_ter[pt] < low_p:
                        low_p = prob_ter[pt]
                if high_p > low_p * 1.5:
                    status = 'bad'
                    f2 = f2 +1
                    print(f2, 'probability imbalance')
                    break   
            # it survives tests
            if status == 'good':
                break
        if status == 'bad':
            # reset everything, break out of for loop
            for n in range(0, 19):
                tile_number[n] = 0
            for tt in terrain:
                prob_ter[tt] = 0
                red_ter[tt] = 0
            break
        # disc is ok
        # print(nt)
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

#balance harbours
# 3:1 harbours must not be adjacent to each other
harb_t = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
h_types = ['3:1',
               '3:1',
               '3:1',
               '3:1',
               'wheat',
               'sheep',
               'wood',
               'brick',
               'ore']
f3 = 0
while True:
    # go through harbour types, pick random location, test for adjacency
    for i in h_types:
        status = 'good'
        # make nine attempts to find good location
        for hat in range(0, 9):
            status = 'good'
            # find location
            while True:
                # p is location
                p = int(9 * random_1())
                # location p not used already
                if harb_t[p] == 'x':
                    break
            # test that previous and next location is not the same
            if i == '3:1':
                # find previous
                before = p - 1
                if before < 0:
                    before = 8
                # find next
                after = p + 1
                if after > 8:
                    after = 0
                if harb_t[before] == '3:1' or harb_t[after] == '3:1':
                    status = 'bad'
                    f3 = f3 + 1
                    print(f3)
                    continue
            if status == 'good':
                harb_t[p] = i
                break        
        # reset the harbours if bad
        if status == 'bad':
            harb_t = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
            break
    # if finished loop at status good, break out
    if status == 'good':
        break    
            
#print errors
print ('number of arrangements of hexagons', f1)
print ('number of arrangements of discs', f2)
print ('number of arrangements of harbours', f3)
print (high_p, ' ', low_p)

print('            ', tile_ter[0], tile_number[0], '  ', tile_ter[1], tile_number[1], '  ', tile_ter[2], tile_number[2])
print('      ', tile_ter[3], tile_number[3], '  ', tile_ter[4], tile_number[4], '  ', tile_ter[5], tile_number[5], '  ', tile_ter[6], tile_number[6])
print(tile_ter[7], tile_number[7], '  ', tile_ter[8], tile_number[8], '  ', tile_ter[9], tile_number[9], '  ', tile_ter[10], tile_number[10], '  ', tile_ter[11], tile_number[11])
print('      ', tile_ter[12], tile_number[12], '  ', tile_ter[13], tile_number[13], '  ', tile_ter[14], tile_number[14], '  ', tile_ter[15], tile_number[15])
print('            ', tile_ter[16], tile_number[16], '  ', tile_ter[17], tile_number[17], '  ', tile_ter[18], tile_number[18])

# print harbours
for m in range(0, 9):
    print(harb_t[m])



