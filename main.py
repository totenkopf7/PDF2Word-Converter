from pdf2docx import Converter, parse
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox


def choose_and_convert_file():
    pdf_file = f"{askopenfilename()}"
    if pdf_file == "":
        messagebox.showwarning("Error", "Please choose a file!")

    else:
        file = pdf_file[:-4]
        word_file = f"{file}.docx"
    # Converter Method
        cv = Converter(pdf_file)
        cv.convert(word_file, start=0, end=None)
        cv.close()

# Parse Method
# parse(pdf_file, word_file, start=0, end=None)

def space():
    space = Label(text="", bg="black")
    space.pack()



root = Tk()

root.title("PDF to Word Converter")
root.geometry("450x450")
root.columnconfigure(0, weight=1)
root.config(bg="black")
root.iconbitmap('icon.ico')

space()
space()
space()

img = PhotoImage(file="logo.png")
pic = Label(root, image=img, bg="black")
pic.pack()

space()
space()
space()
space()
choose_file = Button(width=23, height=1, bg="black", fg="white", text=" Choose and Convert",
                      font=("jost", 11, "bold"), command=choose_and_convert_file)
choose_file.pack()


space()
space()
space()
space()
space()
space()
space()
dev_label = Label(root, text="Developed by Totenkopf 💀", bg="black", fg="#CC1B25", font=("jost", 11))
dev_label.pack()

root.mainloop()

