# gui/step4_exifcopy.py
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from core.exif_manager import batch_copy_tags
from utils.logger import get_logger

logger = get_logger(__name__)

class Step4Widget(QWidget):
    """
    Copies EXIF tags from original JPGs to converted TIFFs using ExifTool.
    """
    def __init__(self, config, on_finish):
        super().__init__()
        self.config = config
        self.on_finish = on_finish
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Ready to copy EXIF tags")
        layout.addWidget(self.label)
        self.btn_copy = QPushButton("Copy EXIF Tags")
        self.btn_copy.clicked.connect(self.copy)
        layout.addWidget(self.btn_copy)
        self.setLayout(layout)

    def copy(self):
        try:
            batch_copy_tags(self.config.exiftool_path, self.config.root_folder, self.config.output_folder)
            self.label.setText("EXIF copy complete.")
            logger.info("EXIF metadata copied.")
            self.on_finish()
        except Exception as e:
            logger.exception("EXIF copying failed: %s", e)
            self.label.setText("EXIF copying failed. Check logs.")
