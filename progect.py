import tkinter as tk
from tkinter import colorchooser, filedialog
import json

class SimpleEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Простий графічний редактор")
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack()

        self.shape = "line"
        self.color = "black"
        self.border_color = "black"
        self.thickness = 1
        self.start_x = self.start_y = None
        self.objects = []
        self.fill_color = "white"


        self.init_menu()
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def init_menu(self):
        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Лінія", command=lambda: self.set_shape("line")).pack(side="left")
        tk.Button(frame, text="Прямокутник", command=lambda: self.set_shape("rect")).pack(side="left")
        tk.Button(frame, text="Еліпс", command=lambda: self.set_shape("oval")).pack(side="left")

        tk.Label(frame, text="Товщина").pack(side="left")
        self.thickness_entry = tk.Entry(frame, width=3)
        self.thickness_entry.insert(0, "1")  # значення за замовчуванням
        self.thickness_entry.pack(side="left")
        tk.Button(frame, text="ОК", command=self.set_thickness).pack(side="left")

        tk.Button(frame, text="Колір рамки", command=self.choose_border_color).pack(side="left")
        tk.Button(frame, text="Заливка фігури", command=self.choose_fill_color).pack(side="left")
        tk.Button(frame, text="Зберегти", command=self.save).pack(side="left")
        tk.Button(frame, text="Завантажити", command=self.load).pack(side="left")


    def set_shape(self, shape):
        self.shape = shape

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def choose_border_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.border_color = color

    def choose_fill_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.fill_color = color

    def set_thickness(self):
        try:
            value = int(self.thickness_entry.get())
            if 1 <= value <= 10:
                self.thickness = value
            else:
                print("Товщина має бути від 1 до 10")
        except ValueError:
            print("Введіть число")

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def stop_draw(self, event):
        x0, y0 = self.start_x, self.start_y
        x1, y1 = event.x, event.y
        shape = None

        if self.shape == "line":
            shape = self.canvas.create_line(x0, y0, x1, y1, fill=self.border_color, width=self.thickness)
        elif self.shape == "rect":
            shape = self.canvas.create_rectangle(x0, y0, x1, y1, outline=self.border_color, fill=self.fill_color,
                                                 width=self.thickness)
        elif self.shape == "oval":
            shape = self.canvas.create_oval(x0, y0, x1, y1, outline=self.border_color, fill=self.fill_color,
                                            width=self.thickness)
        if shape:
            self.objects.append((self.shape, x0, y0, x1, y1, self.fill_color, self.border_color, self.thickness))

    def save(self):
        file = filedialog.asksaveasfilename(defaultextension=".json")
        if file:
            with open(file, "w") as f:
                json.dump(self.objects, f)

    def load(self):
        file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file:
            self.objects.clear()
            with open(file, "r") as f:
                self.objects = json.load(f)
            self.canvas.delete("all")
            for obj in self.objects:
                shape, x0, y0, x1, y1, fill_color, border_color, width = obj
                if shape == "line":
                    self.canvas.create_line(x0, y0, x1, y1, fill=border_color, width=width)
                elif shape == "rect":
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline=border_color, fill=fill_color , width=width)
                elif shape == "oval":
                    self.canvas.create_oval(x0, y0, x1, y1, outline=border_color,fill=fill_color ,width=width)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleEditor(root)
    root.mainloop()

