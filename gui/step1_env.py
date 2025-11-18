# gui/step1_env.py
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog
from utils.config import Config
from utils.logger import get_logger

logger = get_logger(__name__)

class Step1Widget(QWidget):
    """
    Environment selection UI. Sets root folder and resolves default tool paths.
    """
    def __init__(self, config: Config, on_continue):
        super().__init__()
        self.config = config
        self.on_continue = on_continue
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("No root folder selected")
        layout.addWidget(self.label)
        self.btn_select = QPushButton("Select Root Folder")
        self.btn_select.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select)
        self.btn_continue = QPushButton("Set Env Vars and Continue")
        self.btn_continue.clicked.connect(self.set_env)
        layout.addWidget(self.btn_continue)
        self.setLayout(layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Root Folder')
        if folder:
            self.config.root_folder = folder
            self.label.setText(f"Root folder: {folder}")

    def set_env(self):
        if not self.config.root_folder:
            self.label.setText("Please select a root folder first")
            return
        self.config.resolve_paths_from_root()
        logger.info("Environment set: %s", self.config.root_folder)
        self.on_continue()
