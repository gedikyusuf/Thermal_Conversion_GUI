# tests/test_config_paths.py
import pytest
import os
from thermal_converter.utils import Configuration
from thermal_converter.exceptions import PathInitializationError, MissingDependencyError

# Mock root directory for testing purposes
MOCK_ROOT = "/mock/thermal_converter_root"
EXPECTED_DJI_PATH = os.path.join(MOCK_ROOT, 'DJI_Thermal_SDK', 'utility', 'bin', 'windows', 'release_x64', 'dji_irp.exe')
EXPECTED_IMAGEJ_PATH = os.path.join(MOCK_ROOT, 'ImageJ', 'ImageJ', 'ImageJ.exe')

@pytest.fixture
def config_instance():
    """Provides a fresh Configuration instance."""
    return Configuration()

def test_initial_state(config_instance):
    """Test that all paths are None upon initialization."""
    assert config_instance.root_folder is None
    assert config_instance.dji_irp_path is None
    assert config_instance.exiftool_exe_path is None
    assert config_instance.imagej_executable is None
    assert config_instance.macro_file is None

def test_path_initialization_success(config_instance):
    """Tests if path initialization correctly generates expected file paths."""
    config_instance.initialize_paths(MOCK_ROOT)
    
    assert config_instance.root_folder == MOCK_ROOT
    assert config_instance.dji_irp_path == EXPECTED_DJI_PATH
    assert config_instance.imagej_executable == EXPECTED_IMAGEJ_PATH

def test_path_initialization_invalid_root(config_instance):
    """Tests if initialization raises PathInitializationError for invalid root (None)."""
    with pytest.raises(PathInitializationError) as excinfo:
        config_instance.initialize_paths(None)
    
    assert 'invalid' in str(excinfo.value)
    
def test_missing_dependency_raises_error(mocker, config_instance):
    """Tests if validate_paths raises MissingDependencyError when a file is missing."""
    config_instance.initialize_paths(MOCK_ROOT)
    
    mocker.patch('os.path.exists', side_effect=[True, False, True, True]) 
    
    with pytest.raises(MissingDependencyError) as excinfo:
        config_instance.validate_paths()
        
    assert 'ImageJ EXE' in str(excinfo.value)
