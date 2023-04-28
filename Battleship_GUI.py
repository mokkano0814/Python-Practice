from tkinter import *
import pygame
from PIL import ImageTk, Image


def close_rules():
    '''rules_label.forget()
    close_rules_button.forget()
    exit_game_button.pack(side=RIGHT, anchor=SE, padx=button_padding, pady=button_padding)
    rules_game_button.pack(side=RIGHT, anchor=SE, padx=button_padding, pady=button_padding)
    starting_game_button.pack(side=RIGHT, anchor=SE, padx=button_padding, pady=button_padding)'''




def show_rules(widgets):
    widgets['starting_game_button'].forget()
    widgets['rules_game_button'].forget()
    widgets['exit_game_button'].forget()
    rules_text = '''\nPlace your fleet of 3 ships (horizontally or vertically) on your 7X7 Ocean Grid.
You will have a battleship of four -, a cruiser of three -, and a submarine of two cells.
The application will decide who will go first. The computer and You will alternate turns, calling out one shot per turn
to try and hit each other's ships.
On your turn, pick a target hole on your Target Grid and call out its location by letter and number.
If you call out a shot location that occupied by a ship, it's a hit!
If it's not a hit, it's a miss. 
The application automatically saves your hits/misses in another grid.
If the computer or You sink the opponent's entire fleet of 3 ship, the game is over.
'''
    rules_label = Label(widgets['bg_label'], text=rules_text)
    rules_label.pack()
    close_rules_button = Button(widgets['bg_label'], text="Close", command=close_rules)
    close_rules_button.pack()


def game_setup():
    #pygame.mixer.init()
    #pygame.mixer.music.load('bs_menu_music.mp3')
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(0.1)
    start_root = Tk()
    start_root.geometry("1920x1080")
    start_root.title("Battleship")
    start_root.wm_iconbitmap("battleship_icon_171292.ico")

    menu_frame = Frame(start_root, width=1920, height=1000)
    menu_frame.pack()
    menu_frame.pack_propagate(False)

    bg = PhotoImage(file="bs_bg.png")
    bg_label = Label(menu_frame, image=bg)
    bg_label.pack(fill=BOTH, expand=True)

    widgets = creating_buttons(bg_label)

    start_root.mainloop()


def creating_buttons(bg_label):
    button_width = 10
    button_height = 3
    button_padding = 5
    button_style = {
        'font': ('Myriad Pro', 14, 'bold'),
        'bg': 'white',
        'fg': 'black',
        'bd': 0,
        'relief': 'ridge',
        'activebackground': '#CCCCCC',
        'activeforeground': 'black',
        'highlightthickness': 0,
        'highlightbackground': 'white',
        'highlightcolor': 'white',
        'padx': 10,
        'pady': 10,
        'width': button_width,
        'height': button_height,
    }
    exit_game_button = Button(bg_label, text="Exit Game", **button_style)
    exit_game_button.pack(side=RIGHT, anchor=SE, padx=button_padding, pady=button_padding)
    rules_game_button = Button(bg_label, text="Rules", **button_style, command=lambda: show_rules(widgets))
    rules_game_button.pack(side=RIGHT, anchor=SE, padx=button_padding, pady=button_padding)
    starting_game_button = Button(bg_label, text="Start Game", **button_style)
    starting_game_button.pack(side=RIGHT, anchor=SE,padx=button_padding, pady=button_padding)








if __name__ == '__main__':
    game_setup()
    creating_buttons(bg_label)
