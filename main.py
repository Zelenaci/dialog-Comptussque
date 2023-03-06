#!/usr/bin/env python3

import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as mp

class Application(tk.Tk):
    name = "File Plotter"
    title_ = "Plot from file"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.title_)
        self.bind("<Escape>", self.quit)

        self.fileNameVar = tk.StringVar()

        self.file_entry = tk.Entry(self, textvariable=self.fileNameVar)
        self.file_button = tk.Button(self, text="...", command=self.select_file)
        self.draw_button = tk.Button(self, text="Kreslit", command=self.plot)
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)

        self.file_entry.pack()
        self.file_button.pack()
        self.draw_button.pack()
        self.quit_button.pack()

        self.filename = ""

    def select_file(self, event=None):
        self.filename = filedialog.askopenfilename()
        self.fileNameVar.set(self.filename) 

    def plot(self, event=None):
        self.filename = self.fileNameVar.get()
        file_exists = os.path.exists(self.filename)
        x_data = []
        y_data = []

        if file_exists:
            with open(self.filename) as file:
                for line in file:
                    x,y = line.split()
                    x_data.append(x)
                    y_data.append(y)
            fig = mp.subplot()
            fig.plot(x_data, y_data)
        else:
            messagebox.showerror("Soubor neexistuje", "Soubor nebyl nalezen!")

    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()
