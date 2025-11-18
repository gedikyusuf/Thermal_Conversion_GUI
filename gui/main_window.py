# gui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QStackedLayout
from utils.config import Config
from utils.logger import get_logger
from .step1_env import Step1Widget
from .step2_rawgen import Step2Widget
from .step3_convert import Step3Widget
from .step4_exifcopy import Step4Widget
import os

logger = get_logger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thermal Conversion GUI - Modular")
        self.config = Config()
        self._init_ui()

    def _init_ui(self):
        central = QWidget()
        self.stack = QStackedLayout()
        # Step widgets, callbacks navigate stack
        self.step1 = Step1Widget(self.config, on_continue=self.goto_step2)
        self.step2 = Step2Widget(self.config, on_continue=self.goto_step3)
        self.step3 = Step3Widget(self.config, on_continue=self.goto_step4)
        self.step4 = Step4Widget(self.config, on_finish=self.finish)

        self.stack.addWidget(self.step1)
        self.stack.addWidget(self.step2)
        self.stack.addWidget(self.step3)
        self.stack.addWidget(self.step4)
        central.setLayout(self.stack)
        self.setCentralWidget(central)
        self.goto_step1()

    def goto_step1(self):
        self.stack.setCurrentIndex(0)

    def goto_step2(self):
        self.stack.setCurrentIndex(1)

    def goto_step3(self):
        self.stack.setCurrentIndex(2)

    def goto_step4(self):
        self.stack.setCurrentIndex(3)

    def finish(self):
        logger.info("Workflow finished. Output available at %s", self.config.output_folder or os.path.join(os.getcwd(), "converted"))
        self.close()
