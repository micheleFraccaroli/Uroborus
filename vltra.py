#-----------------------------------------------------------------------------
#                                    Vltra
#
#                    ©Copyright 2017 2018 Michele Fraccaroli
#
#
#       This file is part of Vltra.
#
#       Vltra is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       Vltra is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-----------------------------------------------------------------------------
# import string
# import sys
#import fileinput
#import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import functions as f
import plot_total_graph as ptg
import plotting_max as pm
import plotting_subtraction as psub
import multi_plotting as mpl

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

if(os.name == 'nt'):
    os.system('cls')
else:
    os.system('clear')

print(bcolors.MAGENTA + "____   ____.__   __                 " + bcolors.ENDC)
print(bcolors.MAGENTA + "\   \ /   /|  |_/  |_____________   " + bcolors.ENDC)
print(bcolors.OKBLUE +  " \   Y   / |  |\   __\_  __ \__  \  " + bcolors.ENDC)
print(bcolors.OKBLUE +  "  \     /  |  |_|  |  |  | \// __ \_" + bcolors.ENDC)
print(bcolors.CYAN +    "   \___/   |____/__|  |__|  (____  /" + bcolors.ENDC)
print(bcolors.CYAN +    "                                 \/ " + bcolors.ENDC)
print(bcolors.HEADER + "---------------------- Copyright ----------------------\n" + bcolors.ENDC)
print(bcolors.OKBLUE + "Vltra Copyright (C) 2017 2018  Michele Fraccaroli\n" + bcolors.ENDC)
print(bcolors.OKBLUE + "This program comes with ABSOLUTELY NO WARRANTY;\nThis is free software, and you are welcome to redistribute it\nunder certain conditions." + bcolors.ENDC)

try:
    op = f.switch()
    column_x = []
    column_y = []
    file = []

    while 1:
        if op == 'q' or op == 'Q':
            print("\nVltra termined!\n")
            break
    # Plotting total graph -----------------------------------------------
        elif op == '1':
            file = input("Inserisci file .pss: ")
            file_path = ("Input_file/s1_2/" + file)
            try:
                if file != 'q':
                    ptg.plot_total_graph(file_path)
                else:
                    op = f.switch()
            except IOError:
                print("Oops! An error has occurred, try again!\n")
    # Plotting max------------------------------------------------
        elif op == '2':
            # research and plot max of the data ------------------------------------------------------------------------------------
            try:
                if not file:
                    file = input("Inserisci file .pss: ")
                    file_path = ("Input_file/s1_2/" + file)
                    (column_x,column_y) = f.file_import(file_path)

                if file != 'q':
                    interval = input("Inserisci il numero di elemnti in un intervallo per migliorare la precisione dei massimi: ")
                    if interval != 'q':

                        #core of max calculation
                        pm.plotting_max(column_x, column_y, interval)

                        file = input("Inserisci il nome del file con estensione .pss o premi 'q' per terminare: ")
                    else:
                        op = f.switch()
                else:
                    op = f.switch()
            except (IOError, ValueError):
                print("Oops! An error has occurred!\n")

    # Plotting subtraction-----------------------------------------------------------------------------------------------------
        elif op == '3':
            data1 = input('Inserisci il primo file: ')
            data2 = input('Inserisci il secondo file: ')
            data1_path = ("Input_file/s3/" + data1)
            data2_path = ("Input_file/s3/" + data2)
            try:
                if data1 != 'q' or data2 != 'q':
                    psub.plotting_subtraction(data1_path, data2_path, data1, data2)
                else:
                    op = f.switch()
            except IOError:
                print("Oops! An error has occurred, try again!\n")
    # Multi-plotting-----------------------------------------------------------------------------------------------
        elif op == '4':

            files = input("Inserisci file ('ok' per eseguire, 'q' per terminare): ")
            files_path = ("Input_file/s4/" + files)

            if files == 'q' or files == 'Q':
                op = f.switch()
            else:
                mpl.multi_plotting(files, files_path)
    # ------------------------------------------------------------------------------------------------------------
        else:
            print("\nChoice not avaible. Retry!\n")
            op = f.switch()
except (KeyboardInterrupt, EOFError):
    print(bcolors.CYAN + "\n\nVltra termined!\n" + bcolors.ENDC)
