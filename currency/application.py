################################################################################
#   application.py
#
#   Initialization of the App
#
#   06.05.2018  Created by:  zhenya
#   06.02.2019  Last update
################################################################################
from game     import *
from game_gui import *

class Application:
  def __init__(self):
    self.root = Tk()
    self.game = Game()
    self.gui  = GameGUI(self.root, self.game)
