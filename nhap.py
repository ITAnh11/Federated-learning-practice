import tkinter as tk
from PIL import Image, ImageTk

class ImageCutter:
    def __init__(self, root, image_path, rows, cols):
        self.root = root
        self.image_path = image_path
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.cell_images = []
        self.tk_images = [] 
        self.img = Image.open(image_path)
        self.img_width, self.img_height = self.img.size
        self.cell_width = self.img_width // self.cols
        self.cell_height = self.img_height // self.rows
        self.cut_image()

        self.canvas = tk.Canvas(root, width=self.img_width, height=self.img_height)
        self.canvas.pack()
        self.display_cells()
        
    def cut_image(self):
        for row in range(self.rows):
            for col in range(self.cols):
                left = col * self.cell_width
                upper = row * self.cell_height
                right = left + self.cell_width
                lower = upper + self.cell_height
                cell = self.img.crop((left, upper, right, lower))
                self.cells.append(cell)
                self.cell_images.append(cell)
    
    def display_cells(self):
        self.tk_images.clear()  
        for idx, cell in enumerate(self.cell_images):
            row = idx // self.cols
            col = idx % self.cols
            cell_tk = ImageTk.PhotoImage(cell)
            self.tk_images.append(cell_tk) 
            self.canvas.create_image(col * self.cell_width, row * self.cell_height, image=cell_tk, anchor=tk.NW)

    def rotate_cell(self, event, idx):
        cell = self.cells[idx]
        self.cells[idx] = cell.rotate(90)  
        self.cell_images[idx] = self.cells[idx]
        self.canvas.delete("all")  
        self.display_cells()  

    def on_cell_click(self, event):
        col = event.x // self.cell_width
        row = event.y // self.cell_height
        idx = row * self.cols + col
        self.rotate_cell(event, idx)

def main():
    root = tk.Tk()
    root.title("Tool")
    
    image_path = "/home/trang/Pictures/Screenshots/Screenshot from 2025-04-06 10-26-55.png"
    rows, cols = 6, 6  
    app = ImageCutter(root, image_path, rows, cols)
    app.canvas.bind("<Button-1>", app.on_cell_click)
    
    root.mainloop()

if __name__ == "__main__":
    main()