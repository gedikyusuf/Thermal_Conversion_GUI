# gui/step3_convert.py
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from core.imagej_runner import run_imagej_macro
from core.tiff_converter import collect_converted_tifs
from utils.logger import get_logger
import os

logger = get_logger(__name__)

class Step3Widget(QWidget):
    """
    Converts RAW files to TIFF using ImageJ macro (headless).
    """
    def __init__(self, config, on_continue):
        super().__init__()
        self.config = config
        self.on_continue = on_continue
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Ready to convert RAW -> TIFF")
        layout.addWidget(self.label)
        self.btn_convert = QPushButton("Convert RAW to TIFF")
        self.btn_convert.clicked.connect(self.convert)
        layout.addWidget(self.btn_convert)
        self.setLayout(layout)

    def convert(self):
        src = self.config.root_folder
        dest = self.config.output_folder
        os.makedirs(dest, exist_ok=True)
        macro_arg = f"{src}###{dest}"
        try:
            code, out, err = run_imagej_macro(self.config.imagej_executable, self.config.macro_file, macro_arg)
            self.label.setText("ImageJ macro finished.")
            logger.info("ImageJ finished with code %s", code)
            collect_converted_tifs(self.config.root_folder, dest)
            self.on_continue()
        except Exception as e:
            logger.exception("Conversion failed: %s", e)
            self.label.setText("Conversion failed. Check logs.")
