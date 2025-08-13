"""
UI Main Window Design
This file contains the UI layout and design for the main window
"""

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLabel, QMenuBar, QStatusBar, QToolBar, QMainWindow
)
from PyQt5.QtCore import Qt

class Ui_MainWindow:
    def setupUi(self, MainWindow):
        """Setup the UI for the main window"""
        # Set up the central widget
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Create main layout
        self.main_layout = QVBoxLayout(self.centralwidget)
        
        # Create menu bar
        self.menubar = QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        
        # Create toolbar
        self.toolbar = QToolBar(MainWindow)
        MainWindow.addToolBar(self.toolbar)
        
        # Create status bar
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        
        # Create main content area
        self.create_main_content()
        
        # Create menu items
        self.create_menus()
        
        # Create toolbar items
        self.create_toolbar_items()
        
    def create_main_content(self):
        """Create the main content area"""
        # Welcome label
        self.welcome_label = QLabel("Welcome to SIPANDA")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #333;
                margin: 20px;
            }
        """)
        
        # Add welcome label to main layout
        self.main_layout.addWidget(self.welcome_label)
        
        # Create button layout
        self.button_layout = QHBoxLayout()
        
        # Create some example buttons
        self.btn_start = QPushButton("Start")
        self.btn_start.setMinimumSize(120, 40)
        
        self.btn_settings = QPushButton("Settings")
        self.btn_settings.setMinimumSize(120, 40)
        
        self.btn_help = QPushButton("Help")
        self.btn_help.setMinimumSize(120, 40)
        
        # Add buttons to button layout
        self.button_layout.addWidget(self.btn_start)
        self.button_layout.addWidget(self.btn_settings)
        self.button_layout.addWidget(self.btn_help)
        
        # Center the button layout
        self.button_layout.setAlignment(Qt.AlignCenter)
        
        # Add button layout to main layout
        self.main_layout.addLayout(self.button_layout)
        
        # Add some spacing
        self.main_layout.addStretch()
        
    def create_menus(self):
        """Create menu items"""
        # File menu
        self.menu_file = self.menubar.addMenu("File")
        self.action_exit = self.menu_file.addAction("Exit")
        
        # Edit menu
        self.menu_edit = self.menubar.addMenu("Edit")
        self.action_preferences = self.menu_edit.addAction("Preferences")
        
        # Help menu
        self.menu_help = self.menubar.addMenu("Help")
        self.action_about = self.menu_help.addAction("About")
        
    def create_toolbar_items(self):
        """Create toolbar items"""
        # Add some basic toolbar actions
        self.toolbar.addAction("New")
        self.toolbar.addAction("Open")
        self.toolbar.addAction("Save")
        self.toolbar.addSeparator()
        self.toolbar.addAction("Help")