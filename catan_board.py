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
           [0, 4, 7,8],  #D
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
# tiles of the same terrain should not be adjacent

# select terrain tiles in order
# pick random location
# if tile already there pick new location
# if new tile adjacent to one of same terrain
    # reset board, start again
while True:
    # go through terrain tiles
    for n in range(0, 19):
        print(n)
        while True:
            # p is location
            p = int(19 * random_1())
            # find unused tile location
            if tile_ter[p] == 'x':
                break
        # check that location p's terrain is not same as adjacent
        adjacent = 'no'
        for a in adj[p]:
            if tile_ter[a] == ter[n]:
                # adjacent to same thing
                adjacent = 'yes'
                break
        if adjacent == 'yes':
            # reset everything, start over
            tile_ter = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
            break
        # not same as adjacent, so set the tile
        tile_ter[p] = ter[n]
        # repeat loop with new n
    # if loop finished break out
    if adjacent == 'no':
        break
                
                


    
# board of terrain tilse complete

# add number discs to board
# various rules

# select number tokens in order
# pick random location
# if desert or if disc already there pick new location

# test if same-numbered discs are adjacent
# test if same-numbered discs are on same terrain
# test if 6 or 8 are adjacent
# test that 6s, 8s are on four different terrain
# test that the terrain without 6 or 8 has 5 and 9
# test that mountain and hill have 5 and 9

#print board
for x in range(0, 19):
    print(tile_label[x], " ", tile_ter[x])
    








