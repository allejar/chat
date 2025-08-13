from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from ui.ui_main_window import Ui_MainWindow  # Import UI design

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Initialize UI components
        self.setup_ui()
        
        # Initialize data
        self.load_data()
        
        # Connect signals
        self.connect_signals()
        
    def setup_ui(self):
        """Setup UI components and styling"""
        # Set window title
        self.setWindowTitle("SIPANDA - Main Application")
        
        # Set window size
        self.resize(1200, 800)
        
        # Apply styling
        self.apply_styling()
        
    def apply_styling(self):
        """Apply custom styling to the application"""
        # Set application font
        app_font = QFont("Segoe UI", 9)
        self.setFont(app_font)
        
        # Set stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #106ebe;
            }
            QPushButton:pressed {
                background-color: #005a9e;
            }
        """)
        
    def load_data(self):
        """Load initial data for the application"""
        # Show loading status
        self.update_status("Loading data...", 3000)  # 3 second timeout
        
        # TODO: Implement actual data loading logic
        # This could include:
        # - Loading configuration files
        # - Initializing database connections
        # - Loading user preferences
        # - Setting up logging
        
    def connect_signals(self):
        """Connect UI signals to their respective slots"""
        # TODO: Connect button clicks, menu actions, etc.
        pass
        
    def update_status(self, message, timeout=0):
        """Update the status bar with a message
        
        Args:
            message (str): The message to display
            timeout (int): Timeout in milliseconds (0 = no timeout)
        """
        if hasattr(self, 'statusBar'):
            self.statusBar().showMessage(message, timeout)
            
        # Log the status update
        print(f"Status: {message}")
        
    def closeEvent(self, event):
        """Handle application close event"""
        # TODO: Implement cleanup logic
        # - Save user preferences
        # - Close database connections
        # - Clean up temporary files
        
        print("Application closing...")
        event.accept()