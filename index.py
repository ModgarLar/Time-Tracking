import pandas as pd
import math
import json
from datetime import datetime


def __getSheet(sheet_name):
    wb = pd.read_excel('Horario.xlsx', sheet_name=sheet_name)
    datos = wb.to_dict(orient='record')
    return datos

def __getSheetData(sheet_name, datos):
    rows = len(datos)
    obj = {}
    for i in range(rows):
        vals = list(datos[i].values())
        dia = vals[0]
        day = dia.strftime('%d/%m/%y')
        if sheet_name == 'Horario':
            if day not in obj.keys():
                obj[day] = {}
            task = vals[1]
            if task not in obj[day].keys():
                obj[day][task] = 0
            init = vals[2]
            fin = vals[3]
            date1 = datetime.combine(dia, fin)
            date2 = datetime.combine(dia, init)
            time = (date1.minute + date1.hour*60)*60 - (date2.minute + date2.hour*60)*60
            obj[day][task] += int(time / 60)
        elif sheet_name == 'Imputadas':
            time = vals[1]
            obj[day]=time

    return obj

def __getArray(obj):
    data = []
    for day in obj.keys():
        tasks = obj[day]
        for task in tasks.keys():
            time = tasks[task]
            data.append([day, task, time])
    return data


def __getHours(data,input):
    days = input.keys()
    obj = {}
    acum = 0
    for day in days:
        tasks = list(data[day].keys())
        if 'Comida' in tasks:
            data[day].pop('Comida')
        real = sum(list(data[day].values()))
        inputs = input[day]*60
        dif = real - inputs
        acum += dif
        obj[day] = {'real':real,
                    'input':inputs,
                    'dif':dif,
                    'acum':acum}
    return obj


def __getTickets(data):
    obj = {}
    for day in data.keys():
        obj[day] = {}
        tasks = data[day]
        for task in tasks.keys():
            if '-' in task:
                project = task.split('-')[0]
                time =tasks[task]
                if project not in obj[day].keys():
                    obj[day][project] = {}

                if task not in obj[day][project].keys():
                    obj[day][project][task] = time

    return obj

def init():
    datos1 = __getSheet('Horario')
    datos2 = __getSheet('Imputadas')

    data1 = __getSheetData('Horario', datos1)
    data2 = __getSheetData('Imputadas', datos2)
    __getHours(data1, data2)

    tickets = __getTickets(data1)
    print(tickets)

