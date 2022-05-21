# -*- coding: utf-8 -*-
"""

"""

from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from jdlv_data import *
from jdlv_model import *
from jdlv_outils import *

def clean_grid (grid):
    for i in range (default_grid_size):
        for j in range (default_grid_size):
            grid.cases [i][j]['s'] = death_status
            grid.cases [i][j]['c'] = death_color
    return grid

def make_diamond (grid, i, j, color):
    pass

def make_conway (grid, i, j, color):
    try:
        #grid = clean_grid (grid)
        cases = grid.cases
        cases [i] [j] ['s'] = life_status
        cases [i] [j] ['c'] = color
        cases [i] [j + 1] ['s'] = life_status
        cases [i] [j + 1] ['c'] = colors [random.randint(0, 6)]
        cases [i - 1] [j + 1] ['s'] = life_status
        cases [i - 1] [j + 1] ['c'] = colors [random.randint(0, 6)]
        cases [i - 1] [j + 2] ['s'] = life_status
        cases [i - 1] [j + 2] ['c'] = colors [random.randint(0, 6)]
        cases [i - 2] [j + 1] ['s'] = life_status
        cases [i - 2] [j + 1] ['c'] = colors [random.randint(0, 6)]
    except:
        pass
    return grid

def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
               next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
               next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
               next_cases [i] [j] = cases [i] [j]
    return next_grid


def R0_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R1_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 1:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 2 or nbre_alive_voisins >= 5:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R2_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 1:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 3 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R3_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 2:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R4_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 4:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 6:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R5_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 1:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 2:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R6_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 1:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R7_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 1:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 2 or nbre_alive_voisins >= 5:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R8_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 1:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 3 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R9_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 4:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 6:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R10_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 0:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 10 or nbre_alive_voisins >= 50:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid


def R11_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 2:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins < -1 or nbre_alive_voisins >= 8:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R12_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 1:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 0 or nbre_alive_voisins >= 3:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R13_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 0:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins < 0 or nbre_alive_voisins >= 5:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R14_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 1:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R15_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 2:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 5:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid

def R16_rules(grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            if nbre_alive_voisins == 2:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 3 or nbre_alive_voisins >= 7:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid


def manages_rules(texte):
    if texte == "R0":
        apply_game_of_life_rules = R0_rules
    elif texte == "R1":
        apply_game_of_life_rules = R1_rules
    elif texte == "R2":
        apply_game_of_life_rules = R2_rules
    elif texte == "R3":
        apply_game_of_life_rules = R3_rules
    elif texte == "R4":
        apply_game_of_life_rules = R4_rules
    elif texte == "R5":
        apply_game_of_life_rules = R5_rules
    elif texte == "R6":
        apply_game_of_life_rules = R6_rules
    elif texte == "R7":
        apply_game_of_life_rules = R7_rules
    elif texte == "R8":
        apply_game_of_life_rules = R8_rules
    elif texte == "R9":
        apply_game_of_life_rules = R9_rules
    elif texte == "R10":
        apply_game_of_life_rules = R10_rules
    elif texte == "R11":
        apply_game_of_life_rules = R11_rules
    elif texte == "R12":
        apply_game_of_life_rules = R12_rules
    elif texte == "R13":
        apply_game_of_life_rules = R13_rules
    elif texte == "R14":
        apply_game_of_life_rules = R14_rules
    elif texte == "R15":
        apply_game_of_life_rules = R15_rules
    elif texte == "R16":
        apply_game_of_life_rules = R16_rules


def apply_rules (grid, cpt):
    # if (cpt  + 1) % 20 != 0:
    #     #print ("CPT % 11  is  0")
    #     #next_grid = \
    #     #    make_conway (grid, cpt + 4, cpt + 4, 'red')
    #     grid.cases [4] [cpt + 4] = \
    #         revive_case (grid.cases [4] [cpt + 4])
    #     grid.cases [cpt + 4] [20 + 4] = \
    #         revive_case (grid.cases [cpt + 4] [20 + 4])
    #     next_grid = grid
    # else:
    #     cpt = cpt
    #     #print ("CPT % 11 is NOT 0")
    #     time.sleep (0.2)
    #     #next_grid = apply_game_of_life_rules (grid)
    #     grid.cases [cpt - (cpt  + 1) % 20 + 4] [4] = \
    #         revive_case (grid.cases [cpt - (cpt  + 1) % 20 + 4] [4])
    #     next_grid = grid
    next_grid = apply_game_of_life_rules (grid)
    return next_grid

