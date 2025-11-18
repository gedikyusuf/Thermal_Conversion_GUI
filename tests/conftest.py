# tests/conftest.py
import pytest
import sys
from PyQt5.QtWidgets import QApplication

# Gerekirse QApplication fixture'ı kalmalı (önceki adımda eklemiştik)
@pytest.fixture(scope="session", autouse=True)
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    return app

# GLOBAL MOCKING FIXTURE'I: Tüm testler için geçerli olacak
@pytest.fixture(autouse=True)
def mock_path_dependencies(mocker):
    """
    os.path.isdir ve os.path.exists'i tüm test oturumu boyunca taklit eder. 
    Bu, StopIteration hatalarını önler.
    """
    # os.path.isdir: Her zaman True döndür (MOCK_ROOT'un var olduğunu varsayıyoruz)
    mocker.patch('os.path.isdir', return_value=True)

    # os.path.exists: Sadece 'validate_paths' testi için özel olarak tanımlanacak. 
    # Diğer tüm durumlarda (Pytest'in dahili çağrıları dahil) True dönsün.
    mocker.patch('os.path.exists', return_value=True)
