from tkinter import *
import pygame
from PIL import ImageTk, Image





def game_setup():
    def show_rules():
        pass
        starting_game_button.forget()
        rules_game_button.forget()
        exit_game_button.forget()

    def close_rules():
        pass

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

    button_width = 10
    button_height = 3
    button_padding = 5

    button_style = {
        'font': ('Myriad Pro', 16, 'bold'),
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

    rules_game_button = Button(bg_label, text="Rules", **button_style)
    rules_game_button.pack(side=RIGHT, anchor=SE, padx=button_padding, pady=button_padding)
    Battl
    starting_game_button = Button(bg_label, text="Start Game", **button_style)
    starting_game_button.pack(side=RIGHT, anchor=SE, padx=button_padding, pady=button_padding)



    start_root.mainloop()












def exit_game():
    pass

def starting_game():
    pass






if __name__ == '__main__':
    game_setup()
