from gettext import install
from pathlib import Path
from os import *
from tkinter import X, filedialog
from tkinter.ttk import Treeview
from ui import *

# Define functions

def scanDefaultDirs():
    '''Iterates over the provided list to see if the file location exists.'''

    # Create a list of possible locations using the current drive letter
    currentDrive = Path.home().drive

    possibleLocations = []
    possibleLocations.append(currentDrive + "\\Program Files (x86)\Star Trek Online_en\\")

    for location in possibleLocations:
        thisLocation = Path(location)
        if thisLocation.exists():
            print("Install folder exists.")
            global installDirectory
            installDirectory = thisLocation
            current_install_label.configure(text="Install location found: " + str(installDirectory))

def getRecordings():
    global recordingsDirectory
    recordingsDirectory = Path(str(installDirectory) + "\Star Trek Online\Live\demos")

    try:
        for widget in demo_list_frame.winfo_children():
            widget.destroy()
        recordingsList = listdir(recordingsDirectory)
        if (len(recordingsList) > 0):
            createRecordingsTable(recordingsList)
        else:
            recordingsHeader = tk.Label (
                text = "The folder was found, but no recordings exist.",
                master = demo_list_frame
            )
            recordingsHeader.pack()
        return recordingsList
    except:
        current_install_label.configure(text="Install location was not recognised, please try locating again.")
        open_install_button.pack_forget()
        return None

def askInstallDir(event=None):
    '''Opens a directory selection dialog. If demos folder is found it sets the installDirectory and recordingsDirectory respectively.'''

    global installDirectory
    installDirectory = filedialog.askdirectory()
    getRecordings()

def openInstallFolder(event=None):
    startfile(recordingsDirectory)


def createRecordingsTable(recordings):
    recordingsTable = Treeview(
        master=demo_list_frame
    )
    
    recordingsTable['columns'] = ('filename')

    recordingsTable.column("#0", width=0,  stretch="NO")
    recordingsTable.column("filename",anchor="center", width=80)

    recordingsTable.heading("#0",text="",anchor="center")
    recordingsTable.heading("filename",text="Recording Filename",anchor="center")

    recordingsCounter = 0
    for recording in recordings:

        recordingsTable.insert(
            parent='',
            index='end',
            iid=recordingsCounter,
            values=(recording)
            )
        recordingsCounter += 1

    recordingsTable.pack(fill=X)

    open_install_button.pack()
    open_install_button.bind("<Button 1>", openInstallFolder)

# Initialiase variables and attempt to find the installation
installDirectory = None #Set a default value

scanDefaultDirs()

if(installDirectory):
    recordings = getRecordings()

if(recordingsDirectory):
    open_install_button.pack()
    open_install_button.bind("<Button 1>", openInstallFolder)

# Add event listeners
locate_install_button.bind("<Button-1>", askInstallDir)

# Run window main loop to listen for events until close
# (This should be the last line)
mainWindow.mainloop()