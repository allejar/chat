"""
Main Window Controller for SIPANDA Application
Handles the main UI, button connections, and application logic
"""

from PyQt6.QtWidgets import (
    QMainWindow, QMessageBox, QHBoxLayout, QVBoxLayout, 
    QLabel, QWidget, QApplication
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QTimer
from .main_window_ui import Ui_MainWindow
from ui.footer import Footer
from styles import get_main_styles, get_button_styles, get_groupbox_styles
from styles.component_styles import get_camera_styles


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Main application window that inherits from QMainWindow and the generated UI
    """
    
    def __init__(self):
        """Initialize the main window and setup all components"""
        super().__init__()
        
        # Setup the UI from the generated file
        self.setupUi(self)
        
        # Window configuration
        self.setWindowTitle("SIPANDA - Sistem Identifikasi Pangan Digital")
        self.showMaximized()
        
        # Initialize all components
        self._init_ui_layout()
        self._init_footer()
        self._load_styles()
        self._connect_buttons()
        self._set_button_icons()
        self._apply_custom_styles()
        
        # Show initial status
        self.update_status("Aplikasi SIPANDA siap digunakan", 2000)

    def _init_ui_layout(self):
        """Initialize the main UI layout with placeholder sections"""
        # Create main layout for the central widget
        if not self.centralWidget():
            central_widget = QWidget()
            self.setCentralWidget(central_widget)
        
        # Main horizontal layout
        main_layout = QHBoxLayout()
        
        # Left section
        left_section = QLabel("Bagian Kiri\n(Upload & Input)")
        left_section.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_section.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                padding: 20px;
                font-size: 14px;
                font-weight: bold;
                color: #495057;
            }
        """)
        left_section.setMinimumSize(200, 150)
        
        # Center section
        center_section = QLabel("Bagian Tengah\n(Processing & Display)")
        center_section.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center_section.setStyleSheet("""
            QLabel {
                background-color: #e3f2fd;
                border: 2px solid #2196f3;
                border-radius: 8px;
                padding: 20px;
                font-size: 14px;
                font-weight: bold;
                color: #1976d2;
            }
        """)
        center_section.setMinimumSize(300, 150)
        
        # Right section
        right_section = QLabel("Bagian Kanan\n(Results & Export)")
        right_section.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_section.setStyleSheet("""
            QLabel {
                background-color: #f3e5f5;
                border: 2px solid #9c27b0;
                border-radius: 8px;
                padding: 20px;
                font-size: 14px;
                font-weight: bold;
                color: #7b1fa2;
            }
        """)
        right_section.setMinimumSize(200, 150)
        
        # Add sections to layout
        main_layout.addWidget(left_section)
        main_layout.addStretch()
        main_layout.addWidget(center_section)
        main_layout.addStretch()
        main_layout.addWidget(right_section)
        
        # Set the layout to central widget
        self.centralWidget().setLayout(main_layout)

    def _init_footer(self):
        """Initialize the footer component"""
        try:
            self.footer = Footer()
            
            # Get or create main layout for central widget
            if not self.centralWidget().layout():
                self.centralWidget().setLayout(QVBoxLayout())
            
            # Add footer to bottom of main layout
            main_layout = self.centralWidget().layout()
            if isinstance(main_layout, QVBoxLayout):
                main_layout.addWidget(self.footer)
            else:
                # If main layout is horizontal, create a new vertical layout
                vbox = QVBoxLayout()
                vbox.addLayout(main_layout)
                vbox.addWidget(self.footer)
                self.centralWidget().setLayout(vbox)
                
        except Exception as e:
            print(f"Error initializing footer: {e}")
            # Create a simple status bar as fallback
            self.statusBar().showMessage("Footer tidak tersedia")

    def _load_styles(self):
        """Load and apply base styles to the application"""
        try:
            base_style = (
                get_main_styles() + 
                get_button_styles() + 
                get_groupbox_styles()
            )
            self.setStyleSheet(base_style)
        except Exception as e:
            print(f"Error loading styles: {e}")
            # Apply basic fallback styles
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #ffffff;
                }
                QPushButton {
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
            """)

    def update_status(self, message, timeout=0):
        """Update the status message in footer or status bar"""
        try:
            if hasattr(self, 'footer') and self.footer:
                self.footer.showMessage(message, timeout)
            else:
                self.statusBar().showMessage(message, timeout)
        except Exception as e:
            print(f"Error updating status: {e}")
            # Fallback to console output
            print(f"Status: {message}")

    def _apply_custom_styles(self):
        """Apply specific widget styles and properties"""
        try:
            # Button styles
            if hasattr(self, 'btn_start'):
                self.btn_start.setProperty("class", "primary")
            if hasattr(self, 'btn_export'):
                self.btn_export.setProperty("class", "success")
            
            # Status label styling
            if hasattr(self, 'status_label'):
                self.status_label.setStyleSheet("""
                    QLabel {
                        color: #27ae60; 
                        font-weight: bold;
                        font-size: 14px;
                        padding: 5px;
                        background-color: #d5f4e6;
                        border-radius: 4px;
                    }
                """)
            
            # Camera widget styling
            if hasattr(self, 'camera_widget'):
                try:
                    camera_styles = get_camera_styles()
                    self.camera_widget.setStyleSheet(camera_styles)
                except Exception as e:
                    print(f"Error applying camera styles: {e}")
                    
        except Exception as e:
            print(f"Error applying custom styles: {e}")

    def _connect_buttons(self):
        """Connect all buttons to their respective handlers"""
        try:
            # Main control buttons
            if hasattr(self, 'btn_start'):
                self.btn_start.clicked.connect(self._on_start_clicked)
            if hasattr(self, 'btn_export'):
                self.btn_export.clicked.connect(self._on_export_clicked)
            
            # Action buttons
            if hasattr(self, 'btn_upload'):
                self.btn_upload.clicked.connect(self._on_upload_clicked)
            if hasattr(self, 'btn_generateqr'):
                self.btn_generateqr.clicked.connect(self._on_generate_qr_clicked)
            if hasattr(self, 'btn_faceencoding'):
                self.btn_faceencoding.clicked.connect(self._on_face_encoding_clicked)
            if hasattr(self, 'btn_download'):
                self.btn_download.clicked.connect(self._on_download_clicked)
                
        except Exception as e:
            print(f"Error connecting buttons: {e}")

    def _set_button_icons(self):
        """Set icons for all buttons"""
        try:
            icon_paths = {
                'btn_start': 'start',
                'btn_export': 'export',
                'btn_upload': 'upload',
                'btn_generateqr': 'qrcode',
                'btn_faceencoding': 'face',
                'btn_download': 'download'
            }
            
            for btn_name, icon_name in icon_paths.items():
                if hasattr(self, btn_name):
                    button = getattr(self, btn_name)
                    icon_path = f"assets/icons/{icon_name}.png"
                    try:
                        button.setIcon(QIcon(icon_path))
                    except Exception as e:
                        print(f"Error setting icon for {btn_name}: {e}")
                        
        except Exception as e:
            print(f"Error setting button icons: {e}")

    # ==================== BUTTON HANDLERS ====================
    
    def _on_start_clicked(self):
        """Handle start button click"""
        try:
            self.update_status("Memulai aplikasi...", 2000)
            QMessageBox.information(self, "Info", "Aplikasi SIPANDA dimulai!")
            # Add startup logic here
            # Example: self.start_processing()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saat memulai aplikasi: {e}")

    def _on_export_clicked(self):
        """Handle export button click"""
        try:
            self.update_status("Mengexport data...", 2000)
            QMessageBox.information(self, "Info", "Data berhasil di-export!")
            # Add export logic here
            # Example: self.export_data()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saat export: {e}")

    def _on_upload_clicked(self):
        """Handle upload button click"""
        try:
            self.update_status("Upload file...", 2000)
            print("Tombol Upload diklik")
            # Add upload logic here
            # Example: self.upload_file()
        except Exception as e:
            print(f"Error saat upload: {e}")

    def _on_generate_qr_clicked(self):
        """Handle QR generation button click"""
        try:
            self.update_status("Generate QR Code...", 2000)
            print("Generate QR Code")
            # Add QR generation logic here
            # Example: self.generate_qr_code()
        except Exception as e:
            print(f"Error saat generate QR: {e}")

    def _on_face_encoding_clicked(self):
        """Handle face encoding button click"""
        try:
            self.update_status("Proses Face Encoding...", 2000)
            print("Proses Face Encoding")
            # Add face encoding logic here
            # Example: self.process_face_encoding()
        except Exception as e:
            print(f"Error saat face encoding: {e}")

    def _on_download_clicked(self):
        """Handle download button click"""
        try:
            self.update_status("Download data...", 2000)
            print("Download data")
            # Add download logic here
            # Example: self.download_data()
        except Exception as e:
            print(f"Error saat download: {e}")

    # ==================== UTILITY METHODS ====================
    
    def closeEvent(self, event):
        """Handle application close event"""
        try:
            reply = QMessageBox.question(
                self, 
                'Konfirmasi Keluar', 
                'Apakah Anda yakin ingin keluar dari aplikasi?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.update_status("Menutup aplikasi...", 1000)
                event.accept()
            else:
                event.ignore()
        except Exception as e:
            print(f"Error in close event: {e}")
            event.accept()

    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self,
            "Tentang SIPANDA",
            """
            <h3>SIPANDA v1.0</h3>
            <p>Sistem Identifikasi Pangan Digital</p>
            <p>Aplikasi untuk identifikasi dan pengelolaan data pangan</p>
            <p>© 2024 SIPANDA Team</p>
            """
        )

    def show_help(self):
        """Show help dialog"""
        QMessageBox.information(
            self,
            "Bantuan",
            """
            <h3>Panduan Penggunaan SIPANDA</h3>
            <p><b>1. Upload:</b> Upload file gambar pangan</p>
            <p><b>2. Generate QR:</b> Buat kode QR untuk identifikasi</p>
            <p><b>3. Face Encoding:</b> Proses encoding wajah</p>
            <p><b>4. Download:</b> Download hasil data</p>
            <p><b>5. Export:</b> Export data ke format tertentu</p>
            """
        )