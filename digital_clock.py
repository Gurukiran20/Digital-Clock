import tkinter as tk
from time import strftime


def light_theme():
    global frame  # Use global to access the frame defined outside
    frame.destroy()  # Destroy the previous frame
    frame = tk.Frame(root, bg="white")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Time, date, and week display
    lbl_time = tk.Label(frame, font=('calibri', 40, 'bold'),
    background='White', foreground='black')
    lbl_time.pack(anchor="s")
    lbl_date = tk.Label(frame, font=('calibri', 20),
    background='White', foreground='black')
    lbl_date.pack(anchor="n")

    def time():
        string = strftime('%I:%M:%S %p')
        date_str = strftime('%A, %d %B %Y')  # Day of the week, Date, Month, Year
        lbl_time.config(text=string)
        lbl_date.config(text=date_str)
        lbl_time.after(1000, time)
    time()


def dark_theme():
    global frame  # Use global to access the frame defined outside
    frame.destroy()  # Destroy the previous frame
    frame = tk.Frame(root, bg="#22478a")
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    # Time, date, and week display
    lbl_time = tk.Label(frame, font=('calibri', 40, 'bold'),
    background='#22478a', foreground='black')
    lbl_time.pack(anchor="s")
    lbl_date = tk.Label(frame, font=('calibri', 20),
    background='#22478a', foreground='black')
    lbl_date.pack(anchor="n")

    def time():
        string = strftime('%I:%M:%S %p')
        date_str = strftime('%A, %d %B %Y')  # Day of the week, Date, Month, Year
        lbl_time.config(text=string)
        lbl_date.config(text=date_str)
        lbl_time.after(1000, time)
    time()


# Initialize the root window
root = tk.Tk()
root.title("Digital-Clock")
canvas = tk.Canvas(root, height=240, width=500)
canvas.pack()

frame = tk.Frame(root, bg='#22478a')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

lbl_time = tk.Label(frame, font=('calibri', 40, 'bold'),
background='yellow', foreground='black')
lbl_time.pack(anchor="s")
lbl_date = tk.Label(frame, font=('calibri', 20),
background='green', foreground='black')
lbl_date.pack(anchor="n")

def time():
    string = strftime('%I:%M:%S %p')
    date_str = strftime('%A, %d %B %Y')  # Day of the week, Date, Month, Year
    lbl_time.config(text=string)
    lbl_date.config(text=date_str)
    lbl_time.after(1000, time)
time()

# Menu bar for theme selection
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Light", command=light_theme)
theme_menu.add_command(label="Dark", command=dark_theme)
menubar.add_cascade(label="Theme", menu=theme_menu)

root.config(menu=menubar)

root.mainloop()
