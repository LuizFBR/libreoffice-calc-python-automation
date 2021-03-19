import uno  # libreoffice's API
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) # gets parent folder reference to import init.py
from init import init
from time import sleep
from copy import deepcopy

def parse_line(line):
    while line[-1] == 0:
        del line[-1]
    parsed_input = []
    for i in line:
        if i == 0:
            continue
        parsed_input.append(i)
    return parsed_input

def read_line():
    line = list(map(int, input.split()))
    return line

def get_start_point(grid_size, initial_config):
    return (grid_size[1] // 2) - (len(initial_config) // 2) 

def paint_cells(new_generation,current_generation,initial_config,gen,active_sheet,start_point):
    new_generation.insert(0,1)
    new_generation[1] = 1
    new_generation[-1] = abs(new_generation[-2] - 1)
    new_generation.append(1)
    for i in range(start_point - gen,start_point + len(initial_config) + gen): # paint new generation of cells
        list_index = i + gen - start_point
        if (list_index >= 0 and list_index < 2) or (list_index >= len(new_generation) - 2 and list_index < len(new_generation)):
            pass
        else:
            new_generation[list_index] = current_generation[list_index - 2] ^ (current_generation[list_index - 1] or current_generation[list_index])
        if new_generation[list_index] == 1:
            cell = active_sheet.getCellByPosition(i,gen)
            cell.CellBackColor = 1200000 # color is marine blue

def rule_30(document):
    # access the active sheet
    active_sheet = document.CurrentController.ActiveSheet

    initial_config = parse_line([1])  # You can use initial_config = parse_line(read_line()) instead
    number_of_generations = 1000
    time_between_generations = 0.25
    grid_size = (2*number_of_generations - 2 + len(initial_config),number_of_generations)
    start_point = get_start_point(grid_size,initial_config)

    for i in range(start_point,start_point + len(initial_config)):
        cell = active_sheet.getCellByPosition(i,0)
        if initial_config[i - start_point] == 1:
            cell.CellBackColor = 1200000 # color is marine blue
    sleep(5)
    current_generation = deepcopy(initial_config)
    new_generation = deepcopy(current_generation)
    for gen in range(1,number_of_generations):
        print("Gen: {}".format(gen))
        sleep(time_between_generations)
        paint_cells(new_generation,current_generation,initial_config,gen,active_sheet,start_point)
        current_generation = deepcopy(new_generation)

document = init()
rule_30(document)