import tkinter as tk
import pygame.mixer

def game_setup():
    start_root = tk.Tk()
    start_root.geometry("1920x1080")
    start_root.title("Battleship")
    # root.wm_iconbitmap
    start_root.resizable(width=False, height=False)
    game_frame = tk.LabelFrame(start_root, text="Game Board", font=('Myriad Pro', 9), width=650, height=650)
    game_frame.grid(row=0, column=0, padx=30, pady=50)
    game_frame.pack_propagate(False)
    info_frame = tk.LabelFrame(start_root, text="Information / Prepare status", font=('Myriad Pro', 9), width=600,
                               height=600)
    info_frame.grid(row=0, column=1, padx=30, pady=50)
    info_frame.pack_propagate(False)
    start_root.mainloop()
    info_frame_menu = tk.Menu(info_frame




if __name__ == '__main__':
    game_setup()
