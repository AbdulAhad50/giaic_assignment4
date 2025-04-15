import tkinter as tk

# Constants
CELL_SIZE = 40
GRID_WIDTH = 10
GRID_HEIGHT = 10
ERASER_SIZE = 60

class EraserCanvasApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=GRID_WIDTH*CELL_SIZE, height=GRID_HEIGHT*CELL_SIZE)
        self.canvas.pack()

        self.cells = {}  # Store cell ids and their coords

        # Draw grid
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
                self.cells[rect] = (x1, y1, x2, y2)

        # Draw eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray", outline="black", tags="eraser")

        # Bind mouse events
        self.canvas.tag_bind("eraser", "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind("eraser", "<B1-Motion>", self.on_drag)

    def on_press(self, event):
        # Store the initial mouse position
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        # Calculate how far the mouse moved
        dx = event.x - self.start_x
        dy = event.y - self.start_y

        # Move eraser
        self.canvas.move(self.eraser, dx, dy)

        # Update start positions
        self.start_x = event.x
        self.start_y = event.y

        # Get new eraser coordinates
        ex1, ey1, ex2, ey2 = self.canvas.coords(self.eraser)

        # Erase intersecting cells
        for rect, (x1, y1, x2, y2) in self.cells.items():
            if not self._is_erased(rect):  # Only erase blue ones
                if self._rects_overlap((ex1, ey1, ex2, ey2), (x1, y1, x2, y2)):
                    self.canvas.itemconfig(rect, fill="white")

    def _rects_overlap(self, r1, r2):
        # Check if two rectangles overlap
        x11, y11, x12, y12 = r1
        x21, y21, x22, y22 = r2
        return not (x12 < x21 or x11 > x22 or y12 < y21 or y11 > y22)

    def _is_erased(self, rect_id):
        return self.canvas.itemcget(rect_id, "fill") == "white"

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Canvas Eraser Tool")
    app = EraserCanvasApp(root)
    root.mainloop()
