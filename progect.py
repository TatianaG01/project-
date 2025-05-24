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

        def init_menu(self):
            frame = tk.Frame(self.root)
            frame.pack()

        tk.Button(frame, text="Лінія", command=lambda: self.set_shape("line")).pack(side="left")

        tk.Button(frame, text="Прямокутник", command=lambda: self.set_shape("rect")).pack(side="left")
        tk.Button(frame, text="Еліпс", command=lambda: self.set_shape("oval")).pack(side="left")

        tk.Button(frame, text="Колір", command=self.choose_color).pack(side="left")

        tk.Button(frame, text="Зберегти", command=self.save).pack(side="left")
        tk.Button(frame, text="Завантажити", command=self.load).pack(side="left")




if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleEditor(root)
    root.mainloop()




    def stop_draw(self, event):
        x0, y0 = self.start_x, self.start_y
        x1, y1 = event.x, event.y
        shape = None

