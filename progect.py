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

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleEditor(root)
    root.mainloop()

