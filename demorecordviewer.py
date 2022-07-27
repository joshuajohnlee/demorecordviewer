from gettext import install
from pathlib import Path
from os import listdir
from tkinter import filedialog
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
    print("Trying to access " + str(recordingsDirectory))
    try:
        recordingsList = listdir(recordingsDirectory)
        updateRecordingslist(recordingsList)
        return recordingsList
    except:
        print("The demorecord folder was not found")
        return None

def askInstallDir(event=None):
    '''Opens a directory selection dialog. If demos folder is found it sets the installDirectory and recordingsDirectory respectively.'''
    global installDirectory
    installDirectory = filedialog.askdirectory()
    getRecordings()

def updateRecordingslist(recordingsList):
    recordingsHeader = tk.Label (
        text = "The following recordings were found:",
        master = demo_list_frame
    )
    recordingsHeader.pack()
    for recording in recordingsList:
        tk.Label(
            text = recording,
            master = demo_list_frame
        ).pack()


# Initialiase variables and attempt to find the installation
installDirectory = None
scanDefaultDirs()
if(installDirectory):
    getRecordings()

# Add event listeners
locate_install_button.bind("<Button-1>", askInstallDir)


# Run window main loop to listen for events until close
# (This should be the last line)
mainWindow.mainloop()