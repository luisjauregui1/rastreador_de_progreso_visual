from tkinter import *
import json
import os
import datetime

BACKGROUD_COLOR = '#18171c'
LABEL_BG = "#25232e"
LABEL_HIGHLIGHT = "red"
TEXT_COLOR = "white"
JSON_FILE = "data.json"

# Obtener la fecha actual
current_date = datetime.datetime.now()
current_year = str(current_date.year)
current_month = current_date.strftime("%b").upper()  # Nombre del mes en formato abreviado (Ej: "JAN")
current_day = current_date.day

# Ventana principal
window = Tk()
window.title("Rastreador de Progreso")
window.config(padx=20, pady=20, bg=BACKGROUD_COLOR)
window.geometry("1150x950+300+20")
window.resizable(True, True) # Permitimos que la ventana se redimensione

# Label de título
title = Label(window, text=f"HABIT TRACKER - {current_year}", font=("Arial", 16), fg=TEXT_COLOR, bg=BACKGROUD_COLOR)
title.grid(row=0, column=0, columnspan=40, pady=10)

# Frame principal con grid
frame = Frame(window, bg=BACKGROUD_COLOR)
frame.grid(row=1, column=0, padx=10, pady=10)

# Diccionario para almacenar referencias a los labels de días
label_dias = {}
progreso = {}

# Datos de los meses y días
meses = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Cargar progreso desde JSON
def cargar_progreso():
    global progreso
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
            progreso = data.get('progreso', {})

# Guardar progreso en JSON
def guardar_progreso():
    data = {
        "progreso": progreso
    }
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Función para mostrar el calendario y su progreso
def mostrar_calendario():
    global label_dias
    title.config(text=f"Progreso - {current_year}")
    
    for widget in frame.winfo_children():
        widget.destroy()

    label_dias = {}  # Limpiar el diccionario de labels de días
    mostrar_dias()

# Mostrar los días del calendario
def mostrar_dias():
    for i, mes in enumerate(meses):
        Label(frame, text=mes, font=("Arial", 12), fg=TEXT_COLOR, bg=BACKGROUD_COLOR, anchor="w").grid(row=i, column=0, sticky="w", padx=5)

        for j in range(dias_por_mes[i]):
            dia = j + 1
            lbl_dia = Label(frame, text=str(dia), font=("Arial", 9), fg=TEXT_COLOR, bg=LABEL_BG, width=4, height=2, relief="groove", bd=1)
            lbl_dia.grid(row=i, column=j + 1, padx=1, pady=1, sticky="w")

            # Guardamos la referencia en el diccionario con clave (mes, dia)
            label_dias[(mes, dia)] = lbl_dia

            # Deshabilitar días futuros y pasados
            if meses.index(mes) > meses.index(current_month) or (mes == current_month and dia > current_day):
                lbl_dia.config(fg="gray")  # Se muestra en gris para indicar que no es editable
            else:
                # Asignamos un evento de clic a cada día válido
                if dia == current_day and meses.index(mes) == meses.index(current_month):
                    lbl_dia.bind("<Button-1>", lambda event, m=mes, d=dia: marcar_dia(m, d))

        # Cargar el progreso para este calendario
        if mes in progreso:
            for dia, data in progreso[mes].items():
                if (mes, int(dia)) in label_dias:
                    label_dias[(mes, int(dia))].config(fg=LABEL_HIGHLIGHT)

# Función para marcar el progreso en un día
def marcar_dia(mes, dia):
    if meses.index(mes) > meses.index(current_month) or (mes == current_month and dia > current_day):
        return  # No hace nada si el día es futuro

    if mes not in progreso:
        progreso[mes] = {}

    clave = str(dia)

    if clave in progreso[mes]:
        # Si ya está marcado, desmarcarlo
        label_dias[(mes, dia)].config(fg=TEXT_COLOR)
        del progreso[mes][clave]
    else:
        # Marcar como completado
        label_dias[(mes, dia)].config(fg=LABEL_HIGHLIGHT)
        progreso[mes][clave] = {"completed": True,}

    guardar_progreso()

# Cargar progreso al iniciar
cargar_progreso()

# Mostrar calendario inicial
mostrar_calendario()

# Ejecutar ventana
window.mainloop()
