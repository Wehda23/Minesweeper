from tkinter import *
import settings
import utils
from cell import Cell
root = Tk()
# Override the settings of the window
root.configure(bg= "black")
root.geometry("{}x{}".format(settings.WIDTH,settings.HEIGHT))
root.title("Minesweeper game")
root.resizable(False,False)

top_frame = Frame(
    root,
    bg = "black",# Change later to black
    width = utils.width_prct(100),
    height = utils.height_prct(25)

)

top_frame.place(x = 0, y = 0)

game_title = Label(
    top_frame,
    bg= 'black',
    fg = 'white',
    text = 'Minesweeper Game',
    font = ("",48)
)
game_title.place(x= utils.width_prct(25), y= 0)
left_frame = Frame(
    root,
    bg= "black", #change the color later to black
    width = utils.width_prct(25),
    height = utils.height_prct(75),
)
    
left_frame.place(x = 0, y = utils.height_prct(25))

center_frame = Frame(
    root,
    bg = 'black',
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)

center_frame.place(x = utils.width_prct(25),y = utils.height_prct(25))


for x in range(settings.GRIDE_SIZE):
    for y in range(settings.GRIDE_SIZE):
        c = Cell(x = x , y = y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column= x, row = y)
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x= 0, y= 0)

Cell.randomize_mines()

# Run the window
root.mainloop()


