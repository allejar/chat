from PyQt6.QtWidgets import QMainWindow, QMessageBox, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from .main_window_ui import Ui_MainWindow
from ui.footer import Footer
from styles import get_main_styles, get_button_styles, get_groupbox_styles
from styles.component_styles import get_camera_styles

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Initialize UI
        self.setupUi(self)
        self.showMaximized()
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Left section"))
        layout.addStretch()
        layout.addWidget(QLabel("Center section"))
        layout.addStretch()
        layout.addWidget(QLabel("Right section"))
        self.setLayout(layout)
        
        # Initialize components
        self._init_footer()
        self._load_styles()
        self._connect_buttons()
        self._set_button_icons()
        self._apply_custom_styles()

    def _init_footer(self):
        """Alternative using central widget layout"""
        self.footer = Footer()  # As QWidget
        
        # Get or create main layout
        if not self.centralWidget().layout():
            self.centralWidget().setLayout(QVBoxLayout())
        
        # Add footer to bottom of main layout
        self.centralWidget().layout().addWidget(self.footer)

    def _load_styles(self):
        """Load and apply base styles"""
        base_style = (
            get_main_styles() + 
            get_button_styles() + 
            get_groupbox_styles()
        )
        self.setStyleSheet(base_style)

    def update_status(self, message, timeout=0):
        self.footer.showMessage(message, timeout)

    def _apply_custom_styles(self):
        """Apply specific widget styles"""
        # Button styles
        self.btn_start.setProperty("class", "primary")
        self.btn_export.setProperty("class", "success")
        
        # Status label
        if hasattr(self, 'status_label'):
            self.status_label.setStyleSheet("""
                color: #27ae60; 
                font-weight: bold;
                font-size: 14px;
            """)
        
        # Camera widget
        if hasattr(self, 'camera_widget'):
            self.camera_widget.setStyleSheet(get_camera_styles())

    def _connect_buttons(self):
        """Connect all buttons to their handlers"""
        # Main buttons
        self.btn_start.clicked.connect(self._on_start_clicked)
        self.btn_export.clicked.connect(self._on_export_clicked)
        
        # Action buttons
        self.btn_upload.clicked.connect(self._on_upload_clicked)
        self.btn_generateqr.clicked.connect(self._on_generate_qr_clicked)
        self.btn_faceencoding.clicked.connect(self._on_face_encoding_clicked)
        self.btn_download.clicked.connect(self._on_download_clicked)

    def _set_button_icons(self):
        """Set icons for buttons"""
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
                getattr(self, btn_name).setIcon(
                    QIcon(f"assets/icons/{icon_name}.png")
                )

    # --- Button Handlers ---
    def _on_start_clicked(self):
        QMessageBox.information(self, "Info", "Aplikasi dimulai!")
        # Add startup logic here

    def _on_export_clicked(self):
        QMessageBox.information(self, "Info", "Data berhasil di-export!")
        # Add export logic here

    def _on_upload_clicked(self):
        print("Tombol Upload diklik")
        # Add upload logic here

    def _on_generate_qr_clicked(self):
        print("Generate QR Code")
        # Add QR generation logic here

    def _on_face_encoding_clicked(self):
        print("Proses Face Encoding")
        # Add face encoding logic here

    def _on_download_clicked(self):
        print("Download data")
        # Add download logic here