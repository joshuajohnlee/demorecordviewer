from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QPushButton, QVBoxLayout, QWidget, QDialog
from pathlib import Path
from os import listdir
import sys

# Create the Qt App
app = QApplication(sys.argv)

# Initialise variables
installDirectory = ""

# Define functions
def askInstallDir():
    '''Opens a directory selection dialog. If demos folder is found it sets the installDirectory and recordingsDirectory respectively.'''
    installDirectory = str(QFileDialog.getExistingDirectory(window, "Select Star Trek Online install folder"))
    recordingsDirectory = installDirectory + "/Star Trek Online/Live/demos"

    if (recordingsDirectory):
        try:
            recordingsList = listdir(recordingsDirectory)
            print(recordingsList)
        except:
            print("The demorecord folder was not found")
            notFoundError.exec()

# Create layout for main window
button = QPushButton("Find Game Directory")
welcomeMessage = QLabel("Welcome to the DemoRecord Viewer")

# Create layout and add widgets
mainLayout = QVBoxLayout()
mainLayout.addWidget(welcomeMessage)
mainLayout.addWidget(button)
button.clicked.connect(askInstallDir)

# Create main window
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("DemoRecord Viewer")
        self.show()

        widgetContainer = QWidget(self)
        self.setCentralWidget(widgetContainer)
        widgetContainer.setLayout(mainLayout)

window = MainWindow()

# Create error window for later
class Alert(QDialog):
    def __init__(self):
        super(Alert, self).__init__()

# Create layout for error window if directory not found
notFoundError = Alert()
notFoundErrorLayout = QVBoxLayout()

alertText = QLabel("The demo recording folder was not found, please try selecting a different location.")
alertButton = QPushButton("OK")
alertButton.clicked.connect(notFoundError.close)

notFoundErrorLayout.addWidget(alertText)
notFoundErrorLayout.addWidget(alertButton)

notFoundError.setLayout(notFoundErrorLayout)

#Attempt to find default paths for game
currentDrive = Path.home().drive
possibleLocations = []
possibleLocations.append(currentDrive + "\Program Files (x86)\Star Trek Online_en\Star Trek Online\Live\demos")

# Iterate over possible locations to check if they exist
for location in possibleLocations:
    thisLocation = Path(location)
    if thisLocation.exists():
        installDirectory = location
        print("Demo record folder found automatically!")
        label = QLabel("Demo record folder found. The location is " + str(installDirectory))

# If install dir not found, open the dialog window to choose it
if installDirectory == "":
    askInstallDir()

# Exit the application when last main window closed
sys.exit(app.exec_())