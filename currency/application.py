################################################################################
#   initial.py
#
#   Initialization of the App
#
#   06.05.2018  Created by:  zhenya
#   23.05.2018  Last update
################################################################################
from game     import *
from game_gui import *
from valuta   import *

class Application:
  def __init__(self):
    self.game = Game()
    self.root = Tk()
    self.gui  = GameGUI(self.root, self.game)
