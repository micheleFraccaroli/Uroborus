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

import numpy as np
from bisect import bisect
import fileinput
import matplotlib.pyplot as plt
import csv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    MAGENTA = '\033[1;35m'
    CYAN = '\033[1;36m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def point_calc(number_string):
    num = number_string.split('E')
    base = float(num[0])
    exp = float(num[1])
    ris = (base) * 10 ** (exp)
    return ris

def column_creation(row, column_x, column_y, res):
    da_1 = point_calc((row[0]))
    column_x.append(da_1)
    da_2 = point_calc((row[1].strip('\n')))
    column_y.append(da_2)
    res.writerow((da_1, da_2))

def file_import(file):
    f = open(file, "r")
    u = 0
    while u < 2:
        fread_f = f.readline()
        if fread_f[0].isalpha():
            u = u + 1
        else:
            f.seek(0)
            u = u + 1
    fread_f_tot = f.read()
    fread_l = fread_f_tot.count(('\n'))

    f1 = open("file.dat/dati.dat", "w")
    f1.write(fread_f_tot)
    f1.close()
    w = open("file.dat/dati.dat", "r")
    r = open("file.dat/dati.csv", "w")
    # creation file .csv put in 2 columns and generated a data structure
    column_x = []
    column_y = []
    try:
        res = csv.writer(r)
        res.writerow(('D1', 'D2'))
        for i in range(fread_l):
            w1 = w.readline()
            try:
                row = w1.split(" ")
                column_creation(row, column_x, column_y, res)
            except ValueError:
                row = w1.split("\t")
                column_creation(row, column_x, column_y, res)
    finally:
        f.close()
        r.close()

    return column_x, column_y

def file_import_sub(file, i):
    f = open(file, "r")
    u = 0
    while u < 2:
        fread_f = f.readline()
        if fread_f[0].isalpha():
            u = u + 1
        else:
            f.seek(0)
            u = u + 1
    fread_f_tot = f.read()
    fread_l = fread_f_tot.count(('\n'))
    if i == '1':
        f1 = open("file.dat/dati_A.dat", "w")
        f1.write(fread_f_tot)
        f1.close()
        w = open("file.dat/dati_A.dat", "r")
        r = open("file.dat/dati_A.csv", "w")
    else:
        f1 = open("file.dat/dati_A2.dat", "w")
        f1.write(fread_f_tot)
        f1.close()
        w = open("file.dat/dati_A2.dat", "r")
        r = open("file.dat/dati_A2.csv", "w")
    # creation file .csv put in 2 columns and generated a data structure
    column_x_1 = []
    column_y_1 = []
    try:
        res = csv.writer(r)
        res.writerow(('D1', 'D2'))
        for i in range(int(fread_l/2)):
            w1 = w.readline()
            try:
                row = w1.split("\t")
                column_creation(row, column_x_1, column_y_1, res)
            except ValueError:
                row = w1.split(" ")
                column_creation(row, column_x_1, column_y_1, res)
    finally:
        f.close()
        r.close()

    return column_x_1, column_y_1

def draw_line():
    lines = []
    ax = plt.gca()
    xy = plt.ginput(2,timeout=-1)
    x = [p[0] for p in xy]
    y = [p[1] for p in xy]
    line = plt.plot(x,y,marker = 'd', color = 'black', linestyle='--')
    ax.figure.canvas.draw()
    lines.append(line)
    return x,y,ax,lines[0]

def del_lines(ax):
    x = plt.ginput(1)
    ax.lines.pop(1)
    ax.lines.pop(1)
    # np1,np2,ax,line = draw_line()

def line_result(np1,np2,line,cx,cy):
    p1 = []
    p2 = []
    coef1 = np.polyfit(np1,np2,1)

    idx1 = line[0].get_xdata()[0]
    idx2 = line[0].get_xdata()[1]

    #print(ax.lines.pop(1))
    # index
    x1 = bisect(cx,idx1)
    x2 = bisect(cx,idx2)

    #resizing lists for new plot
    del cx[0:x1-1]
    del cx[x2+1:len(cx)]
    del cy[0:x1-1]
    del cy[x2+1:len(cy)]

    # draw the line from user

    # coords for result
    Imax = cy.index(max(cy))
    Ymax = max(cy)
    Xmax = cx[Imax]

    Yfinded = coef1[0]*Xmax + coef1[1]

    p1.append(Xmax)
    p1.append(Xmax)
    p2.append(Ymax)
    p2.append(Yfinded)
    res_line = plt.plot(p1,p2)
    return Yfinded, cy

def switch():
    op = input(bcolors.HEADER + "\n --------------------- Make choice ---------------------\n\n" + bcolors.ENDC + bcolors.WARNING + "1)" + bcolors.ENDC + " Plotting total graph\n"+ bcolors.WARNING + "2)"+ bcolors.ENDC + " Max of graph\n"+ bcolors.WARNING + "3)"+ bcolors.ENDC + " Subtraction between graphs\n"+ bcolors.WARNING + "4)" + bcolors.ENDC + " Multi-plotting graph\n\n"+bcolors.FAIL+"=>"+bcolors.ENDC+" ('"+ bcolors.FAIL + "q"+ bcolors.ENDC + "' for term the app): ")
    return op
# -------------------------------------------
