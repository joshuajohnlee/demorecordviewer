import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

# Create main window
mainWindow = tk.Tk()
mainWindow.title("DemoRecord Viewer by JoystickJoshy")
mainWindow.geometry("600x720")
mainWindow.minsize(600, 600)
mainWindow.columnconfigure(0, weight=1, minsize=75)
mainWindow.rowconfigure([0, 1], weight=1, minsize=50)

# Create frames
welcome_frame = tk.Frame()
demo_list_frame = tk.Frame()
controls_frame = tk.Frame()
bottom_info_frame = tk.Frame(
    relief="ridge",
    borderwidth=5,
)

# Create text
welcome_label = tk.Label(
    text = "Welcome to the DemoRecord Viewer!",
    master = welcome_frame,
    font=('Arial', 25)
)
welcome_label.pack()

current_install_label = tk.Label(
    text = None,
    master = bottom_info_frame
)
current_install_label.pack()


# Create buttons
locate_install_button = tk.Button(
    text = "Locate Installation",
    width = 20,
    height = 2,
    master = controls_frame
)
locate_install_button.pack()

open_install_button = tk.Button(
    text = "Open Install Folder",
    width = 20,
    height = 2,
    master = controls_frame
)

# Grid positioning for frames
welcome_frame.grid(
    row=0, 
    column=0, 
    padx=10, 
    pady=3,
    sticky="ew",
)

demo_list_frame.grid(
    row=1,
    column=0,
    padx=5, 
    pady=3,
    sticky="new",
)

controls_frame.grid(
    row=2,
    column=0,
    padx=5, 
    pady=3,
    sticky="ew",
)

bottom_info_frame.grid(
    row = 3,
    column = 0,
    padx=5, 
    pady=3,
    sticky="sew",
)