import uno
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) # gets parent folder reference to import init.py
from init import init
from time import sleep
from copy import deepcopy # for debugging purposes

def read_matrix():

    size = list(map(int, input().split()))
    sizeR = size[0]
    sizeC = size[1]

    matrix = [[0] * sizeC for row in range(0, sizeR)]
    for x in range(0, sizeR):

        line = list(map(int, input().split()))

        for y in range(0, sizeC):
            matrix[x][y] = line[y]

    return matrix


def adjust_game(game_size, initial_config): #centers matrix initial_config in game_size matrix
    half_x = len(initial_config[0])//2
    half_y = len(initial_config)//2

    matrix = [[0] * game_size[1] for row in range(0, game_size[0])]

    live_cells = []

    for i in range(len(initial_config)):
        for j in range(len(initial_config[0])):
            matrix[i - half_x + game_size[0]//2][j - half_y + game_size[1]//2] = initial_config[i][j]
            if initial_config[i][j] == 1:
                live_cells.append((i - half_x + game_size[0]//2,j - half_y + game_size[1]//2))

    return matrix, live_cells

def parse_neighborhood(game_size, live_cells, neighbor_cells):
    for cell in live_cells:
        if (cell not in neighbor_cells): # add living cells to neighbor_cells if they aren't in the list
            neighbor_cells[(cell[0],cell[1])] = 0 
        for i in range(-1,2):
            for j in range(-1,2): # add living cell neighbors to neighbor_cells or increase their living neighbor cell count if they're already in the list
                if cell[0] + i < 0 or cell[0] + i >= game_size[0] or cell[1] + j < 0 or cell[1] + j >= game_size[1] or (i == 0 and j == 0):
                    continue
                if (i + cell[0],j + cell[1]) not in neighbor_cells:
                    neighbor_cells[(i + cell[0],j + cell[1])]  = 1
                else:
                    neighbor_cells[(i + cell[0],j + cell[1])] += 1

def game_of_life(document):
    active_sheet = document.CurrentController.getActiveSheet()

    number_of_generations = 10000
    game_size = (15,15) # set the matrix the game will run in
    time_between_generations = 0.25

    initial_config = [[0,1,0],
                      [0,0,1],
                      [1,1,1]]

    
    game_grid, live_cells = adjust_game(game_size, initial_config)
    for row in game_grid:
        for cell in row:
            print(cell, end = " ")
        print()

    print("live_cells: {}".format(live_cells))

    sleep(5)
    for cell in live_cells: # paint the live cells in Calc
        calcCell = active_sheet.getCellByPosition(cell[1],cell[0])
        calcCell.CellBackColor = 1200000
    
    neighbor_cells = {}
    for gen in range(1,number_of_generations):
        parse_neighborhood(game_size, live_cells, neighbor_cells)
        live_cells.clear()
        sleep(time_between_generations)
        for cell in neighbor_cells:
            calcCell = active_sheet.getCellByPosition(cell[1],cell[0])
            if neighbor_cells[cell] < 2 or neighbor_cells[cell] > 3: # Then, by isolation or overpopulation, the cell dies
                game_grid[cell[0]][cell[1]] = 0
                calcCell.CellBackColor = 16777215 # color is white
            elif neighbor_cells[cell] == 3: # Then, by repopulation, the cell comes to life
                game_grid[cell[0]][cell[1]] = 1
                live_cells.append(cell) 
                calcCell.CellBackColor = 1200000 # color is marine blue
            elif neighbor_cells[cell] == 2 and game_grid[cell[0]][cell[1]] == 1: # if cell was alive, it continues to live, therefore we must append it to our live_cells list
                live_cells.append(cell)
        neighbor_cells.clear()
        print("Generation: {}".format(gen))


document = init()
game_of_life(document)
