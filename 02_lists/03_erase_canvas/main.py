import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraseCanvas:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        
        self.eraser = None
        self.create_grid()
        self.create_eraser()
        
        # Mouse click event to activate the eraser
        self.canvas.bind("<B1-Motion>", self.erase)

    def create_grid(self):
        """Create a grid of blue cells"""
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                self.canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue")

    def create_eraser(self):
        """Create the eraser (a pink square)"""
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

    def erase(self, event):
        """Erase cells in contact with the eraser"""
        mouse_x = event.x
        mouse_y = event.y
        
        # Move the eraser to the mouse position
        self.canvas.coords(self.eraser, mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
        
        # Find overlapping rectangles to erase
        overlapping_items = self.canvas.find_overlapping(mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE)
        for item in overlapping_items:
            if self.canvas.itemcget(item, "fill") == "blue":
                self.canvas.itemconfig(item, fill="white")

def main():
    root = tk.Tk()
    root.title("Erase Canvas")
    app = EraseCanvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
