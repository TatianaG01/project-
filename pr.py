from tkinter import colorchooser


def set_shape(self, shape):
    self.shape = shape

def choose_color(self):
    color = colorchooser.askcolor()[1]
    if color:
        self.color = color

def start_draw(self, event):
    self.start_x = event.x
    self.start_y = event.y
















