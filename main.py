import tkinter as tk
import index
from tkinter import ttk
function_names = [func for func in dir(index) if not func.startswith('__')]
for func in function_names:
    print(func)
    if getattr(index,func).__class__.__name__ == 'function':
        pass
        #print(func)
root = tk.Tk()

def addButton(frame,name, colour,side):
    button = tk.Button(frame,text=name,fg=colour)
    button.pack(side=side)

def dropdown(frame,values,side):
    combo = ttk.Combobox(frame)
    combo['values']=values
    combo.pack(side=side)
root.geometry("200x80")
topFrame = tk.Frame(root)
topFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack(side=tk.BOTTOM)

dropdown(topFrame,('Tickets','Time Tracking','Horario'),tk.BOTTOM)
addButton(bottomFrame,'Submit','black',tk.TOP)

root.mainloop()

