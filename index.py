import pandas as pd
import json
from datetime import datetime

cols = [0,1,2,3]
wb = pd.read_excel('Horario.xlsx',sheet_name='Horario', encoding='utf8')
data = wb.to_dict(orient='record')
rows = len(wb)
cols = 4
obj = {}
for i in range(rows):
    vals = data[i]
    dia = vals['Dia']
    day = dia.strftime('%d/%m/%y')
    if day not in obj.keys():
        obj[day] = {}
    task = vals['Tarea']
    if task not in obj[day].keys():
        obj[day][task] = 0
    init = vals['Hora Inicio']
    fin = vals['Hora Final']
    time = datetime.combine(dia,fin) - datetime.combine(dia,init)
    obj[day][task] += int(time.seconds/60)

data = []

for day in obj.keys():
    tasks = obj[day]
    for task in tasks.keys():
        time = tasks[task]
        data.append([day,task,time])