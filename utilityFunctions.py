from enum import Enum

class ReplayStatus(Enum):
    OK = 1
    DUPLICATE = 2
    NOK = 3