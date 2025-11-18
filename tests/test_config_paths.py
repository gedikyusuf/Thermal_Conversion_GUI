# tests/test_config_paths.py
import pytest
import os
from thermal_converter.utils import Configuration
from thermal_converter.exceptions import PathInitializationError, MissingDependencyError

# ... (MOCK_ROOT ve EXPECTED_PATH tanımları) ...

@pytest.fixture
def config_instance():
    return Configuration()

def test_initial_state(config_instance):
    # ... (Bu test başarılı, dokunmuyoruz) ...
    pass

def test_path_initialization_success(mocker, config_instance): # <-- mocker ekle
    """Tests if path initialization correctly generates expected file paths."""
    
    # Mocker: os.path.isdir'i taklit et, her zaman True döndür
    mocker.patch('os.path.isdir', return_value=True) 

    config_instance.initialize_paths(MOCK_ROOT)
    
    # ... (Geri kalan assert'ler, başarılı olacak) ...
    assert config_instance.root_folder == MOCK_ROOT
    assert config_instance.dji_irp_path == EXPECTED_DJI_PATH
    assert config_instance.imagej_executable == EXPECTED_IMAGEJ_PATH


def test_missing_dependency_raises_error(mocker, config_instance):
    """Tests if validate_paths raises MissingDependencyError when a file is missing."""
    
    # Mocker: os.path.isdir'i taklit et (True)
    mocker.patch('os.path.isdir', return_value=True) 
    
    # Mocker: os.path.exists'i taklit et (İlk 1 True, sonraki 3 False olacak)
    mocker.patch('os.path.exists', side_effect=[True, False, True, True]) 
    
    config_instance.initialize_paths(MOCK_ROOT)

    with pytest.raises(MissingDependencyError) as excinfo:
        config_instance.validate_paths()
        
    assert 'ImageJ EXE' in str(excinfo.value)
