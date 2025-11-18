# tests/conftest.py
import pytest
import sys
from PyQt5.QtWidgets import QApplication

# 1. PyQt5 Sanal Ortamı (Katman 1 çözümü)
@pytest.fixture(scope="session", autouse=True)
def qapp():
    # ... (QApplication başlatma mantığı) ...
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    return app

# 2. Windows Komutlarını ve Dosya Yollarını Taklit Etme (Katman 2 & 3 çözümü)
@pytest.fixture(autouse=True)
def mock_path_and_subprocess(mocker):
    """Tüm subprocess çağrılarını ve os.path kontrolünü taklit eder."""
    
    # Katman 3 Çözümü: Subprocess çağrılarını her zaman başarılı olarak taklit et
    # Bu, testlerin Windows komutlarını çalıştırmasını engeller.
    mocker.patch('subprocess.run', return_value=mocker.Mock(returncode=0))
    mocker.patch('subprocess.Popen', return_value=mocker.Mock())

    # Katman 2 Çözümü: os.path.isdir'i taklit et (klasör var kabul et)
    # Bu, initialize_paths metodunuzdaki hatayı çözer.
    mocker.patch('os.path.isdir', return_value=True)
