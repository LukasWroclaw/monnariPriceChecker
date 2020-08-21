from enum import Enum

class ReplayStatus(Enum):
    OK = 1
    DUPLICATE = 2
    NOK = 3
    
class FiltersOption(Enum):
    CHANGED_ONLY = 1
    ZERO_PRICE = 2
    PROMOD = 3
    MONNARI = 4
    QUIOSQUE = 5