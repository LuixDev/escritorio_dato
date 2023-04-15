import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

class Ventana2:
    def __init__(self, master):
        self.master = master
        self.master.title("Insertar")
        self.master.geometry("900x500")
        self.frame = tk.Frame(self.master)
        self.frame.config(bg="white")
       
        self.frame.place(x=0, y=0, width=900, height=500)
        

        self.label1 = tk.Label(self.frame, text="Fecha", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label1.place(x=50, y=120)
        self.caja01 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja01.place(x=190, y=130)

        self.label2 = tk.Label(self.frame, text="Ciudad", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label2.place(x=50, y=170)
        self.caja02 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja02.place(x=190, y=180)

        self.label3 = tk.Label(self.frame, text="Pasajeros/dia", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label3.place(x=50, y=220)
        self.caja03 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja03.place(x=190, y=230)

        self.label4 = tk.Label(self.frame, text="Variación Transmilenio", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label4.place(x=50, y=270)
        self.caja04 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja04.place(x=250, y=280)

        self.label5 = tk.Label(self.frame, text="Pasajeros día típico laboral", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label5.place(x=400, y=120)
        self.caja05 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja05.place(x=620, y=130)

        self.label6 = tk.Label(self.frame, text="Pasajeros día sábado", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label6.place(x=400, y=170)
        self.caja06 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja06.place(x=620, y=180)


        self.label7 = tk.Label(self.frame, text="Pasajeros día domingo", font=("Arial", 13), bg='#FFFFFF', fg='black' )
        self.label7.place(x=50, y=50)
        self.caja07 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja07.place(x=250, y=50)

        self.label8 = tk.Label(self.frame, text="Pasajeros día festivo", font=("Arial", 13), bg='#FFFFFF', fg='black' )
        self.label8.place(x=450, y=220)
        self.caja08 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja08.place(x=620, y=230)
                          
        self.label9 = tk.Label(self.frame, text="DíaSemana", font=("Arial", 13), bg='#FFFFFF', fg='black', )
        self.label9.place(x=450, y=270)
        self.caja09 = tk.Entry(self.frame, font=("Arial", 12), bg="white", fg="black", bd=2, relief="groove")
        self.caja09.place(x=620, y=280)

        
        
        
        self.button = tk.Button(self.frame, text="Insertar" , command=lambda: guardar_registro(self, self.caja01.get(), self.caja02.get(),self.caja03.get(), self.caja04.get(), self.caja05.get(), self.caja06.get(), self.caja07.get(), self.caja08.get() ,self.caja09.get()))
        self.button.place(x=420,y=330)


def guardar_registro(ventana, columna1,columna2,columna3,columna4,columna5,columna6,columna7,columna8,columna9):
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='adata'
    )

    # Crear un cursor para realizar operaciones en la base de datos
    cursor = conexion.cursor()

    # Insertar los datos en la tabla correspondiente
    consulta = "INSERT INTO transporte (COL1,COL2,COL3,COL4,COL5,COL6,COL7,COL8,COL9 ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    valores = (columna1,columna2,columna3,columna4,columna5,columna6,columna7,columna8,columna9)
    cursor.execute(consulta, valores)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    # Cerrar la conexión y el cursor
    cursor.close()
    conexion.close()

    messagebox.showinfo("Registro guardado", "se ha guadado en la base de dato.")

      
if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana2(root)
    root.mainloop()
