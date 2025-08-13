#!/usr/bin/env python3
"""
SIPANDA Main Application Entry Point
"""

import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow  # Import class controller

def main():
    """Main application entry point"""
    # Create the Qt application
    app = QApplication(sys.argv)
    
    # Create and show the main window
    main_window = MainWindow()
    main_window.show()
    
    # Start the event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()