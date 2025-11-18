# gui/step2_rawgen.py
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from core.raw_processor import generate_raw
from utils.logger import get_logger

logger = get_logger(__name__)

class Step2Widget(QWidget):
    """
    Starts RAW generation (invokes DJI SDK tool). Provides simple status feedback.
    """
    def __init__(self, config, on_continue):
        super().__init__()
        self.config = config
        self.on_continue = on_continue
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel("Ready to generate RAW files")
        layout.addWidget(self.label)
        self.btn_run = QPushButton("Generate RAW Files")
        self.btn_run.clicked.connect(self.run)
        layout.addWidget(self.btn_run)
        self.setLayout(layout)

    def run(self):
        ok = generate_raw(self.config.dji_folder and self.config.dji_folder + os.sep + "dji_irp.exe", self.config.root_folder)
        if ok:
            self.label.setText("RAW generation started. Proceed to next step.")
            logger.info("RAW generation initiated.")
            self.on_continue()
        else:
            self.label.setText("RAW generation failed or unsupported on this platform.")
