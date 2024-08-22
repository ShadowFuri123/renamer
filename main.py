from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog, messagebox
import os
import subprocess

number_photo = 0
path = ''
files = []

def center_window(window):
    window.update_idletasks()
    width = 500
    height = 200
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def choose_path():
    global number_photo, path, files
    number_photo = 0
    try:
        path = filedialog.askdirectory()
        files = os.listdir(path)
        show_photo()
    except:
        pass

def show_photo(condition=False):
    global number_photo, path, files
    if condition:
        subprocess.call("TASKKILL /F /IM PhotosApp.exe")
    try:
        photo = Image.open(fr'{path}\\{files[number_photo]}')
    except:
        if number_photo >= len(files):
            messagebox.showerror("Ошибка", 'Файлы в папке закончились')
            choose_path()
        else:
            messagebox.showerror('Ошибка', 'Файл не является фото')
    photo.show()

def next_photo():
    global number_photo
    number_photo += 1
    show_photo(condition=True)

def rename():
    global number_photo, path, files
    name = entry.get()
    type = files[number_photo].split('.')[-1]
    os.rename(f'{path}//{files[number_photo]}', f'{path}//{name}.{type}')
    number_photo += 1
    entry.delete(0, len(entry.get()))
    show_photo(True)

def finish():
    root.destroy()


root = tkinter.Tk()
center_window(root)
root.protocol('WM_DELETE_WINDOW', finish)

image = ImageTk.PhotoImage(file='choose_direct.png')

but_ch = tkinter.Button(root, image=image, command=choose_path).place(x=20, y= 100, height=70, width=70)
but_con = tkinter.Button(root, text='Далее', font='Times 24', command=next_photo).place(x=120, y=100, height=70, width=130)
but_rename = tkinter.Button(root, text='Переименовать', font='Times 24', command=rename).place(x=270, y=100, height=70, width=220)

entry = tkinter.Entry(root, font='Times 30')
entry.place(x=20, y=10, height=70, width=470)

root.mainloop()

