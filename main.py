import tkinter as tk
from cli import cli_main
from gui import start_gui


def Run_Selection():
    def launch_gui():
        root.destroy()
        start_gui() 

    def launch_cli():
        root.destroy()
        cli_main()  

    root = tk.Tk()
    root.title("Select Mode")
    root.geometry("300x120")

    label = tk.Label(root, text="Choose how to run the program:", font=("Arial", 12))
    label.pack(pady=10)

    gui_btn = tk.Button(root, text="GUI Mode", width=20, command=launch_gui)
    gui_btn.pack(pady=5)

    cli_btn = tk.Button(root, text="CLI Mode", width=20, command=launch_cli)
    cli_btn.pack(pady=5)

    root.mainloop()

#Run by default 
Run_Selection()
