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


import copy as cp
import functions as f
import numpy as np
import matplotlib.pyplot as plt
from bisect import bisect
from matplotlib.widgets import Button


def plot_total_graph(file_path):
    (column_x,column_y) = f.file_import(file_path)
    # plotting array column
    trace1 = plt.plot(column_x,column_y)

    title = input("Inserisci il titolo del grafico: ")
    xname = input("Inserisci il nome dell'asse x: ")
    yname = input("Inserisci il nome dell'asse y: ")
    #plt.grid('on')
    plt.suptitle(title, fontsize=12, fontweight='bold')
    plt.xlabel(xname, fontsize=20)
    plt.ylabel(yname, fontsize=20)
    plt.tick_params(labelsize=16)

    # creation and plotting interactive line
    while True:
        try:
            cx = cp.deepcopy(column_x)
            cy = cp.deepcopy(column_y)
            np1,np2,ax,line = f.draw_line()
            Yfinded,cys = f.line_result(np1,np2,line,cx,cy)
            print("\n--------------------\nMAX: " + str(max(cys) - Yfinded) + "\n--------------------\n")
            f.del_lines(ax)
        except Exception:
            exit()
    # result
    plt.show()
