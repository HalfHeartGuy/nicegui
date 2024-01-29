
from nicegui import ui

import os
current_folder = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_folder, 'Jugendwettbewerb_Statistics.csv')
# read data from csv file
with open(csv_file_path, 'r') as f:
    data = f.readlines()




column_row = data[0].replace('\n', '')
columns_csv = column_row.split(';')
columns_nicegui = [
    {'name': oneColumn, 'label': oneColumn, 'field': oneColumn, 'required': True, 'align': 'left', 'sortable':True} for oneColumn in columns_csv
]

print(f"columns", columns_nicegui)

data_csv = data[1:] # e.g.['Stufe1-4;23;18;14;10;1;2023',...]
new_data_csv = []
for oneStufe in data_csv:
    oneStufe = oneStufe.replace("\n","")
    new_data_csv.append(oneStufe.split(";"))
data_csv = new_data_csv
data_nicegui = data_csv
one_row_dict = []
for onerow in data_nicegui:

    one_row_dict.append({"Jahrgang":onerow[0],"Geschlecht": onerow[1], "1.Preis":onerow[2],"2.Preis":onerow[3],"Auszeichnung": onerow[4], "Anerkennung":onerow[5], "Runde":onerow[6], "Jahr":onerow[7]})
#for oneLine in data_csv:
 #   one_row = oneLine.split(';') # List of values of one record, z.B. ['Stufe1-4', '23', '18', '14', '10', '1', '2023']

    #one_row_dict =
'''
rows = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 21},
    {'name': 'Carol'},
]
'''

rund1_table = ui.table(columns=columns_nicegui, rows=one_row_dict, row_key='Jahrgangstufe',pagination=10)


ui.run()
