from tkinter import BOTH, YES, Canvas, Tk

from line import Line


class Window:
    def __init__(self, width, height) -> None:
        self.__running = False
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title = "Maze solver"

        self.__canvas = Canvas(width=width, height=height, bg="white")
        self.__canvas.pack(expand=YES, fill=BOTH)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False
