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

column_x_1 = []
column_y_1 = []
column_x_2 = []
column_y_2 = []
column_ris = []
trace_ris = []

def plotting_subtraction(data1_path, data2_path, data1, data2):

	leg_check = input("Vuoi la legenda?(Y,n): ")
	if leg_check == 'Y' or leg_check == 'y':
		legend = input("Inserisci legenda: ")

	while(data1 != 'ok' or data2 != 'ok'):
	    (column_x_1, column_y_1) = f.file_import_sub(data1_path, 1)
	    (column_x_2, column_y_2) = f.file_import_sub(data2_path, 2)

	    for i in range(len(column_y_1)):
	        column_ris.append(float(column_y_1[i]) - float(column_y_2[i]))

	    if leg_check == 'Y' or leg_check == 'y':
	        trace_ris.append(plt.plot(column_x_1, column_ris, label=legend))
	    else:
	        trace_ris.append(plt.plot(column_x_1, column_ris))
	    column_ris.clear()
	    data1 = input("Inserisci il primo file('ok' per eseguire): ")
	    data2 = input("Inserisci il secondo file('ok' per eseguire): ")
	    data1_path = ("Input_file/s3/" + data1)
	    data2_path = ("Input_file/s3/" + data2)
	    if data1 == 'ok' or data2 == 'ok':
	        break
	    else:
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

	np1,np2 = f.draw_line()
	plt.plot(np1,np2, marker = 'd', color = 'black', linestyle='--')

	plt.show()
