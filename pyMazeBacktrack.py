import libtcodpy as libtcod
from random import randint

nSquares = 30
nTiles = nSquares * 2 + 1

SCREEN_WIDTH = nTiles
SCREEN_HEIGHT = nTiles

libtcod.console_set_custom_font("cp437_12x12.png", libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'pyMazeBacktrack', False, libtcod.RENDERER_OPENGL)

def CheckDir(x,y,size,direction,table):

    if direction == 1:
        if y - 2 <= 0:
            return 0
        if table[x][y-2] == white:
            return 0
    elif direction == 2:
        if x + 2 >= size:
            return 0
        if table[x+2][y] == white:
            return 0
    elif direction == 3:
        if y + 2 >= size:
            return 0
        if table[x][y+2] == white:
            return 0
    elif direction == 4:
        if x - 2 <= 0:
            return 0
        if table[x-2][y] == white:
            return 0
    
    return 1

def Possible(x,y,table,size):

    if x+2 < size:
        if table[x+2][y] == black:
            return 1
    if x-2 > 0:
        if table[x-2][y] == black:
            return 1
    if y+2 < size:
        if table[x][y+2] == black:
            return 1
    if y-2 > 0:
        if table[x][y-2] == black:
            return 1        

    return 0

black = libtcod.black
white = libtcod.white

Table = [[0 for i in range(nTiles)]for i in range(nTiles)]

for x in range(nTiles):
    for y in range(nTiles):
        Table[x][y] = black
        libtcod.console_put_char_ex(None,x,y,219,Table[x][y],libtcod.white)

libtcod.console_flush()

Memory = []

CurrX = 1
CurrY = 1
Table[CurrX][CurrY] = white

end = 0

while end == 0:

    while Possible(CurrX,CurrY,Table,nTiles):

        Dir = randint(1,4)
        while CheckDir(CurrX,CurrY,nTiles,Dir,Table) == 0:
            Dir = randint(1,4)

        if Dir == 1:
            Table[CurrX][CurrY - 1] = white
            CurrY -= 2
            Table[CurrX][CurrY] = white
        elif Dir == 2:
            Table[CurrX + 1][CurrY] = white
            CurrX += 2
            Table[CurrX][CurrY] = white
        elif Dir == 3:
            Table[CurrX][CurrY + 1] = white
            CurrY += 2
            Table[CurrX][CurrY] = white
        elif Dir == 4:
            Table[CurrX - 1][CurrY] = white
            CurrX -= 2
            Table[CurrX][CurrY] = white

        Memory.append(Dir)

        #print
        for x in range(nTiles):
            for y in range(nTiles):
                libtcod.console_put_char_ex(None,x,y,219,Table[x][y],libtcod.white)
        libtcod.console_flush()

    while Possible(CurrX,CurrY,Table,nTiles) == 0:

        MemorySize = len(Memory)

        Dir = Memory[MemorySize-1]

        if Dir == 1:
            CurrY += 2
        elif Dir == 2:
            CurrX -= 2
        elif Dir == 3:
            CurrY -= 2
        elif Dir == 4:
            CurrX += 2

        del Memory[MemorySize-1]

        if CurrX == 1 and CurrY == 1:
            end = 1
            break

#print
for x in range(nTiles):
    for y in range(nTiles):
        libtcod.console_put_char_ex(None,x,y,219,Table[x][y],libtcod.white)
libtcod.console_flush()

libtcod.console_wait_for_keypress(True)





























    
