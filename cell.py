from tkinter import Button, Label
import random
import settings
import ctypes
import sys 


class Cell:
    all : list = []
    cell_count_label_object = None
    cells_count = settings.CELL_COUNT
    def __init__(self, x,y, is_mine = False,) -> None:
        self.is_mine : bool = is_mine
        self.is_opened : bool = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        
        #Append the object to Cell.all list
        Cell.all.append(self)

    def create_btn_object(self,location) -> None:
        btn : Button = Button(
            location,
            width =12,
            height= 4,
           
        )
        btn.bind("<Button-1>",self.left_click_actions) # Left Click
        btn.bind("<Button-3>",self.right_click_actions) # Right Click

        self.cell_btn_object : Button = btn

    @staticmethod
    def create_cell_count_label(location):
        label : Label = Label(
            location,
            bg = "black",
            fg = "white",
            text = f"Cells Left:{Cell.cells_count}",
            width = 12,
            height = 4,
            font = ("",30)
        )
        
        Cell.cell_count_label_object : Label = label
    
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()

            self.show_cell()
            # if mines counts = cells left count, player won
            if Cell.cells_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'Congratulations you won the game!',"Game Over", 0)

        # Cancel left and right clicked events if cell is already opened.
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")


    
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine.',"Game Over", 0)
        
        sys.exit()
        
    def get_cell_by_axis(self , x, y):
        # Return cell object based on the value of x and y.
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    @property
    def surrounded_cells(self) -> list:
        # Create an empty list to hold coordinates
        temp : list = []
        # Create two pointers to use multiple pointers algorithms
        left, right = self.x - 1, self.y - 1
        # Create while loop to extract the surrounding existing cells dynamically.
        while left < self.x + 2:
            # Make sure the Y axis of cell is not below 0 or greater than Gride Size and in Range 
            if (right >= 0 and right < settings.GRIDE_SIZE and right < self.y + 2):
                # Make sure the X axis of cell is not below 0 or greater than Gride Size and in Range 
                if (left >= 0 and left < settings.GRIDE_SIZE and left < self.x + 2):
                    # Filter current clicked cell coordinate to clear confusion.
                    if not(left == self.x and right == self.y):
                        temp.append([left,right])
            # Moving Vertically Y axis increment by 1 
            if right <= self.y + 1:
                right += 1
            # Else reset Y axis and move horizontally incrementing X axis by 1 and reset Y axis.
            else:
                right = self.y - 1
                left += 1

        # Get all surrounding cell objects dynamically.    
        cells : list = [self.get_cell_by_axis(x,y) for x,y in temp]

        return cells
    
    @property
    def surrounded_cells_mines_length(self) -> int:
        counter = 0 

        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cells_count -= 1
            self.is_opened = True
            
        self.cell_btn_object.configure(text= self.surrounded_cells_mines_length)
        # Replace the text of cell count label with a newer count.
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(text = f"Cells Left:{Cell.cells_count}")

        self.cell_btn_object.configure(
            bg = 'SystemButtonFace'
        )
        

    def right_click_actions(self,event):
        if not(self.is_mine_candidate):
            self.cell_btn_object.configure(
                bg = 'orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg = "SystemButtonFace"
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells : list[Cell] = random.sample(
            Cell.all,
            settings.MINES_COUNT
        )
        for cell in picked_cells:
            cell.is_mine = True
        
        


    def __repr__(self):
        return f"Cell({self.x},{self.y})"