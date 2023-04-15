import pandas as pd
import mysql.connector
from pandastable import Table
import tkinter as tk

class Ventana3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Virtualizar")
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.show()

    def show(self):
        # Obtener los datos de la base de datos
        cnx = mysql.connector.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='adata')
        cursor = cnx.cursor()
        query = "SELECT * FROM transporte"

        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        cnx.close()

        

      
        

        # Crear el DataFrame de pandas
        data = pd.DataFrame(data, columns=["fecha", "ciudad", "Sistema", "Pasajeros/dia", "Variación Transmilenio", "pasajeros día típico laboral", "Pasajeros día sábado", "Pasajeros día festivo", "DíaSemana"])

        # Eliminar columnas vacías
        data.dropna(axis=1, how='all', inplace=True)

        # Crear la tabla con múltiples columnas
        self.table = Table(self.frame, dataframe=data, showtoolbar=True, showstatusbar=True, editable=False, ncols=len(data.columns))
        self.table.show()
        self.table.bind_all("<Key>", self.key_pressed)

    def key_pressed(self, event):
        print(f"Tecla presionada: {event.char}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana3(root)
    root.mainloop()







