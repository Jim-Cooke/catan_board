# Program to generate random Catan boards

# import libraries
import random
import time
import math
import array

#board - position 0 to 18
#    00  01  02
#  03  04  05  06
#07  08  09  10  11
#  12  13  14  15
#    16  17  18

# tile_label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']
tile_ter = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
# terrain types: 1 desert, 4 field, 4 pasture, 4 forest, 3 hill, 3 mountain
tile_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

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



# create board with terrain tiles

# select terrain tiles in order
# pick random location
# if tile already there pick new location

f1 = 0    

# go through terrain tiles
for n in ter:
    # print(n)
    while True:
        # p is location
        p = int(19 * random_1())
        # find unused tile location
        if tile_ter[p] == 'x':
            break
    # place the tile
    tile_ter[p] = n
    # repeat loop with new n
  
  
# board of terrain tiles complete

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
            # reset everything, break out of for loop
            tile_number = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

# test if 6 or 8 are adjacent-done

#harbours
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

# go through harbour types, pick random location, test for adjacency
for i in h_types:
    # find location
    while True:
        # p is location
        p = int(9 * random_1())
        # location p not used already
        if harb_t[p] == 'x':
            break
    harb_t[p] = i



#print errors
print ('number of arrangements of hexagons', f1)
print ('number of arrangements of discs', f2)
print ('number of arrangements of harbours', f3)


print('            ', tile_ter[0], tile_number[0], '  ', tile_ter[1], tile_number[1], '  ', tile_ter[2], tile_number[2])
print('      ', tile_ter[3], tile_number[3], '  ', tile_ter[4], tile_number[4], '  ', tile_ter[5], tile_number[5], '  ', tile_ter[6], tile_number[6])
print(tile_ter[7], tile_number[7], '  ', tile_ter[8], tile_number[8], '  ', tile_ter[9], tile_number[9], '  ', tile_ter[10], tile_number[10], '  ', tile_ter[11], tile_number[11])
print('      ', tile_ter[12], tile_number[12], '  ', tile_ter[13], tile_number[13], '  ', tile_ter[14], tile_number[14], '  ', tile_ter[15], tile_number[15])
print('            ', tile_ter[16], tile_number[16], '  ', tile_ter[17], tile_number[17], '  ', tile_ter[18], tile_number[18])

# print harbours
for m in range(0, 9):
    print(harb_t[m])


