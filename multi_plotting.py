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


import functions as f
import matplotlib.pyplot as plt

column_x = []
column_y = []
trace = []

def multi_plotting(files, files_path):
	i = 0
	leg_check = input("Vuoi la legenda?(Y,n): ")

	if leg_check == 'Y' or leg_check == 'y':
	    legend = input("Inserisci legenda: ")

	if files == 'q' or files == 'Q':
	    op = f.switch()
	else:
	    try:
	        while (files != 'ok'):
	            (column_x, column_y) = f.file_import(files_path)
	            if leg_check == 'Y' or leg_check == 'y':
	                trace.append(plt.plot(column_x, column_y, label=legend))
	            else:
	                trace.append(plt.plot(column_x, column_y))
	            i = i + 1
	            files = input("Inserisci file ('ok' per eseguire, 'q' per terminare): ")
	            files_path = ("Input_file/s4/" + files)
	            if files != 'ok' and leg_check == 'Y' or leg_check == 'y':
	                legend = input("Inserisci legenda: ")

	        if leg_check == 'Y' or leg_check == 'y':
	            let = plt.legend()
	            let.draggable()
	        title = input("Inserisci il titolo del grafico: ")
	        xname = input("Inserisci il nome dell'asse x: ")
	        yname = input("Inserisci il nome dell'asse y: ")

	        plt.suptitle(title, fontsize=12, fontweight='bold')
	        plt.xlabel(xname)
	        plt.ylabel(yname)
	        plt.tick_params(labelsize=30)

	        np1,np2 = f.draw_line()
	        plt.plot(np1,np2, marker = 'd', color = 'black', linestyle='--')

	        plt.show()
	    except IOError:
	        print("Oops! An error has occurred, try again!\n")
