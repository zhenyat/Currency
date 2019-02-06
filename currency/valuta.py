################################################################################
#   valuta.py
#
#   Model:  Class Currency  
#
#   10.05.2018  Created by:  zhenya
################################################################################
import json
import os.path
import random
import time

class Currency():
  def __init__(self):
    self.valuta = {
      'США':       'доллар', 'Россия':   'рубль',  'Азербайджан': 'манат', 
      'Албания':   'лек',    'Монголия': 'тугрик', 'Молдавия':    'лей',
      'Германия':  'евро',   'Индия':    'рупия',  'Канада':      'доллар',
      'Израиль':   'шекель', 'Ирак':     'динар',  'Казахстан':   'тенге',
      'Аргентина': 'песо',   'Польша':   'злотый', 'Грузия':      'лари',
      'Китай':     'юань',   'Армения':  'драм',   'Корея':       'вона',
      'Швейцария': 'франк',  'Япония':   'йена',   'ЮАР':         'рэнд', 
      'Египет':    'фунт',   'Швеция':   'крона',  'Афганистан':  'афгани',
      'Исландия':  'крона',  'Иран':     'риал',   'Турция':      'лира'
    }
    
    self.update_data('valuta.json')
    self.countries = list(self.valuta.keys())
    
  def reset(self):
    random.seed(time.time())
    random.shuffle(self.countries)
    
  # Gets data from a file <filename> and updates valuta dictionary
  def update_data(self, filename):
    if os.path.isfile(filename):
      with open(filename) as json_file:
        self.valuta = json.load(json_file)

