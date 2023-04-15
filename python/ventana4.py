import tkinter as tk
from PIL import Image, ImageTk

class Ventana4:
    def __init__(self, master):
        self.master = master
        self.master.title("Acerca")
        self.master.geometry("800x400")
        self.master.title("Acerca")
        self.frame = tk.Frame(self.master)
        self.frame.config(bg="white")
        self.img1 = ImageTk.PhotoImage(Image.open("dow.jpeg"))
        tk.Label(self.frame, image=self.img1).pack()
        
        self.frame.pack()
        
       
        self.label = tk.Label(self.frame, text="MINERIA DE DATO", font=("Arial", 13), bg='#FFFFFF', fg='black' )
        self.label.pack()
        self.label1 = tk.Label(self.frame, text="INTEGRANTE: Luis rodriguez , Ronaldo sara , Aldemar morales", font=("Arial", 13), bg='#FFFFFF', fg='black')
        self.label1.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Ventana4(root)
    root.mainloop()
