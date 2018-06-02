################################################################################
#   game_gui.py
#
#   GUI for the Game Application (aka View)
#   Instance arguments:
#     master  - Root Window
#     game    - Game instance 
#
#   10.05.2018  Created by:  zhenya
#   23.05.2018  Last update
################################################################################
from tkinter import *

class GameGUI:
  def __init__(self, master, game):
    self.master = master
    
    # Default attribures
    master.title('Угадай валюту страны')
    master.geometry(self.center(master))
    master.attributes("-topmost", True)
    master.config(background = 'lightyellow')

    # Widgets
    self.left_frame = Frame(master, width=300, height=400, background='lightgreen')
    self.left_frame.grid(row=0, sticky=W)
    
    self.label_question = Label(self.left_frame, text="Страна", background='lightgreen')
    self.label_question.grid(row=0, sticky=E)
    self.label_question.columnconfigure(0, minsize=10)
    
    self.question_box = Text(self.left_frame, width = 20, height = 1, bg = 'light cyan')
    self.question_box.grid(row = 0, column = 1, sticky = W)
    
    self.label_reply = Label(self.left_frame, text="Назови валюту:", bg='lightgreen')
    self.label_reply.grid(row=0, column = 2, sticky=E)
    
    self.reply_box = Entry(self.left_frame, width = 10, bg = 'alice blue', bd = 5)
    self.reply_box.grid(row = 0, column = 3, sticky = W)
    
    self.reply_button = Button(self.left_frame, text='Ответить', highlightbackground ="dark green", command=game.reply)
    self.reply_button.grid(row=0, column=4, sticky=W)
    self.reply_button.config(state=DISABLED)

    self.result_box = Text(self.left_frame, width = 80, height = 20, bg = 'beige')
    self.result_box.grid(row = 1, column = 0, columnspan = 5, sticky = W)
    
    self.bottom_frame = Frame(master, width=300, background='light cyan')
    self.bottom_frame.grid(row=1, sticky=W)
    
    self.start_button = Button(self.bottom_frame, text="Начать", highlightbackground ="grey", command=lambda: game.start(self))
    self.start_button.grid(row=0)
    
    self.quit_button  = Button(self.bottom_frame, text="Закончить", highlightbackground ="grey", command=game.quit)
    self.quit_button.grid(row=0, column=1)

  # Locates GUI window in the center of a screen
  def center(self, master):
    masterWidth  = 800
    masterHeight = 600
    
    screenWidth  = master.winfo_screenwidth()
    screenHeight = master.winfo_screenheight()
    
    masterX = (screenWidth  - masterWidth)  / 2
    masterY = (screenHeight - masterHeight) / 2
    
    return('%dx%d+%d+%d' % (masterWidth, masterHeight, masterX, masterY))
