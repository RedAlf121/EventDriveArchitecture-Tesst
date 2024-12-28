from enum import Enum


class ArriveStates(Enum):
    NotChecked=0
    Travelling=1
    NotPostChecked = 2
    Checked = 3