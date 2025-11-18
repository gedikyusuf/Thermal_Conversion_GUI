# tests/test_config_paths.py
import pytest
import os
from thermal_converter.utils import Configuration
from thermal_converter.exceptions import PathInitializationError, MissingDependencyError

# tests/test_config_paths.py (Güncellenmiş Kısımlar)

# ... (gerekli importlar) ...

# test_path_initialization_success (TEMİZLENMİŞ HALİ)
def test_path_initialization_success(config_instance): # <-- mocker fixture'ını kaldırdık!
    """Tests if path initialization correctly generates expected file paths."""
    
    # Mocker çağrısı burada yok, conftest.py'deki global mock kullanılacak.
    config_instance.initialize_paths(MOCK_ROOT)
    
    assert config_instance.root_folder == MOCK_ROOT
    # ... diğer assert'ler ...

# test_missing_dependency_raises_error (SADECE side_effect'i geri ekle)
def test_missing_dependency_raises_error(mocker, config_instance):
    """Tests if validate_paths raises MissingDependencyError when a file is missing."""
    
    # Bu testin özel bir side_effect'e ihtiyacı var, bu yüzden onu override ediyoruz.
    mocker.patch('os.path.exists', side_effect=[
        True,      # DJI IRP (Var)
        False,     # ImageJ EXE (Yok - Hata fırlatılmalı)
        True, True, True, True, True, True, True, True, True, True # Yeterli yedek
    ], autospec=True) # autospec, daha katı hata kontrolü sağlar.

    config_instance.initialize_paths(MOCK_ROOT)

    with pytest.raises(MissingDependencyError) as excinfo:
        config_instance.validate_paths()
        
    assert 'ImageJ EXE' in str(excinfo.value)
