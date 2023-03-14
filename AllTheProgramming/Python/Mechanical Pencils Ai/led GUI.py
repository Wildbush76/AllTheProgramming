from tkinter import *




def thing():
    print("stupid")
    pass

if __name__ == "__main__":
    window = Tk()
    #window.bind("<Return>",thing
    window.geometry("800x700")
    window.configure(background="#FF7F50")
    window.title("LED GUI")
    window.resizable(width=False,height=False)

    button = Button(width=2,height=1,fg="#FFFFFF")
    button.pack()
    
