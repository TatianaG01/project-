import tkinter as tk

class SimpleEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Простий графічний редактор")
        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack()

        self.shape = "line"
        self.color = "black"
        self.border_color = "black"
        self.thickness = 2
        self.start_x = self.start_y = None
        self.objects = []

        self.init_menu()
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        def init_menu(self):
            frame = tk.Frame(self.root)
            frame.pack()

        tk.Button(frame, text="Лінія", command=lambda: self.set_shape("line")).pack(side="left")

        tk.Button(frame, text="Прямокутник", command=lambda: self.set_shape("rect")).pack(side="left")
        tk.Button(frame, text="Еліпс", command=lambda: self.set_shape("oval")).pack(side="left")

        tk.Button(frame, text="Колір", command=self.choose_color).pack(side="left")

        tk.Button(frame, text="Зберегти", command=self.save).pack(side="left")
        tk.Button(frame, text="Завантажити", command=self.load).pack(side="left")

        def set_shape(self, shape):
            self.shape = shape

        def choose_color(self):
            color = colorchooser.askcolor()[1]
            if color:
                self.color = color

        def start_draw(self, event):
            self.start_x = event.x
            self.start_y = event.y


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleEditor(root)
    root.mainloop()




    def stop_draw(self, event):
        x0, y0 = self.start_x, self.start_y
        x1, y1 = event.x, event.y
        shape = None

         if self.shape == "line":
            shape = self.canvas.create_line(x0, y0, x1, y1, fill=self.color, width=self.thickness)
        elif self.shape == "rect":
            shape = self.canvas.create_rectangle(x0, y0, x1, y1, outline=self.color, width=self.thickness)
        elif self.shape == "oval":
            shape = self.canvas.create_oval(x0, y0, x1, y1, outline=self.color, width=self.thickness)
        if shape:
            self.objects.append((self.shape, x0, y0, x1, y1, self.color, self.thickness))

    def save(self):
        file = filedialog.asksaveasfilename(defaultextension=".json")
        if file:
            with open(file, "w") as f:
                json.dump(self.objects, f)


    def load(self):
        file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file:
            with open(file, "r") as f:
                self.objects = json.load(f)
            self.canvas.delete("all")
            for obj in self.objects:
                shape, x0, y0, x1, y1, color, width = obj
                if shape == "line":
                    self.canvas.create_line(x0, y0, x1, y1, fill=color, width=width)
                elif shape == "rect":
                    self.canvas.create_rectangle(x0, y0, x1, y1, outline=color, width=width)
                elif shape == "oval":
                    self.canvas.create_oval(x0, y0, x1, y1, outline=color, width=width)


