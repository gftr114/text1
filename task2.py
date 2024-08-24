import time

class Pupil:
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

pupil = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.surname, pupil.name, "-" ,pupil.mark)
    print("\n")
