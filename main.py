from tkinter import Tk
from 주소록 import AddressBook

if __name__ == '__main__':
    root = Tk()
    application = AddressBook(root, "Demo Application - Objects in Python")
    root.mainloop()
