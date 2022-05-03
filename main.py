from tkinter import *
from tkmacosx import Button  # For MacOS
from cell import *
import settings
import utils

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(root, bg="black", width=settings.WIDTH, height=utils.height_prct(25))
top_frame.place(x=0, y=0)

left_frame = Frame(root, bg="black", width=utils.width_prct(25), height=utils.height_prct(75))
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(root, bg="black", width=utils.width_prct(75), height=utils.height_prct(75))
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

# btn1 = Button(center_frame, bg="red", text="First Button")
# btn1 = Button(center_frame, bg="blue", text="First Button", borderless=1)  # For MacOS
# btn1.place(x=0, y=0)

# c1 = Cell()
# c1.create_btn_object(center_frame)
# # c1.cell_btn_object.place(x=0, y=0)
# c1.cell_btn_object.grid(column=0, row=0)
#
# c2 = Cell()
# c2.create_btn_object(center_frame)
# # c2.cell_btn_object.place(x=40, y=0)
# c2.cell_btn_object.grid(column=0, row=1)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

# Run the window
root.mainloop()
