from tkinter import *
from tkinter import messagebox
import json
import os

BACKGROUD_COLOR = '#18171c'

# Ventana principal
window = Tk()
window.title("rastreador de progreso visual")
window.config(padx=20, pady=20, bg=BACKGROUD_COLOR)
window.geometry("1150x950+300+20")  # posición y dimensión fija de ventana
window.resizable(False, False)

# Label de título
title = Label(text="HABIT TRACKER", font=("Arial", 16), fg="white", bg=BACKGROUD_COLOR)
title.pack()

# Frame para los meses y días, anclado a la izquierda
frame = Frame(window, bg=BACKGROUD_COLOR)
frame.pack(anchor='w')

# Meses del año y número de días por mes (año no bisiesto)
meses = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Para cada mes, coloca el nombre en la columna 0 y los días a la derecha en la misma fila
for i, mes in enumerate(meses):
    # Coloca el nombre del mes en la columna 0
    label_mes = Label(frame, text=mes, font=("Arial", 12), fg="white", bg=BACKGROUD_COLOR, anchor="w")
    label_mes.grid(row=i, column=0, padx=1, pady=1, sticky="w")
    
    for j in range(dias_por_mes[i]):
        dia = j + 1
        # Se crea un canvas para cada día
        canvas = Canvas(frame, width=30, height=30, bg=BACKGROUD_COLOR, highlightthickness=0)
        canvas.grid(row=i, column=j+1, padx=1, pady=1, sticky="w")
        
        # Dibuja un círculo blanco, delgado y sencillo
        canvas.create_oval(5, 5, 25, 25, outline="white", width=1)
        
        # Dibuja el número centrado dentro del círculo
        canvas.create_text(15, 15, text=str(dia), font=("Arial", 9), fill="white")

# Frame para los controles (botones) en la parte inferior
bottom_frame = Frame(window, bg=BACKGROUD_COLOR)
bottom_frame.pack(side=BOTTOM, fill=X, pady=10)

# Botones en el frame inferior
btn_start = Button(bottom_frame, text="Start", font=("Arial", 12), fg="white", bg="#4CAF50", relief=FLAT)
btn_start.pack(side=LEFT, padx=10)

btn_pause = Button(bottom_frame, text="Pause", font=("Arial", 12), fg="white", bg="#f39c12", relief=FLAT)
btn_pause.pack(side=LEFT, padx=10)

btn_reset = Button(bottom_frame, text="Reset", font=("Arial", 12), fg="white", bg="#e74c3c", relief=FLAT)
btn_reset.pack(side=LEFT, padx=10)

btn_quit = Button(bottom_frame, text="Quit", font=("Arial", 12), fg="white", bg="#7f8c8d", relief=FLAT, command=window.quit)
btn_quit.pack(side=LEFT, padx=10)

window.mainloop()
