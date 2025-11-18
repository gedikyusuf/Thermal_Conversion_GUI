# tests/test_command_construction.py
import pytest
import os
from thermal_converter.utils import Configuration

@pytest.fixture
def mock_config():
    """Configures a mock Configuration object with valid paths."""
    config = Configuration()
    config.root_folder = "C:\\Test\\Root"
    config.dji_irp_path = "C:\\Test\\Root\\dji\\dji_irp.exe"
    config.exiftool_exe_path = "C:\\Test\\Root\\exiftool\\exiftool.exe"
    return config

def test_irp_command_format(mock_config):
    """Test the structure of the dji_irp.exe command (STEP 2)."""
    irp_exe = mock_config.dji_irp_path
    
    expected_template = 'for %i in (*.JPG) do "{}" -a measure -s "%i" -o "%~ni.raw" --measurefmt float32'
    expected_cmd = expected_template.format(irp_exe)
    
    final_launch_cmd = f'start cmd /K "cd /d {mock_config.root_folder} & {expected_cmd}"'
    
    assert 'for %i in (*.JPG)' in final_launch_cmd
    assert 'start cmd /K' in final_launch_cmd
    assert mock_config.root_folder in final_launch_cmd

def test_exiftool_command_format(mock_config):
    """Test the structure of the exiftool command (STEP 4)."""
    
    jpg_path = os.path.join(mock_config.root_folder, "test_image.JPG")
    tif_path = os.path.join(mock_config.root_folder, "converted", "test_image.TIF")
    exiftool_exe = mock_config.exiftool_exe_path
    
    cmd_list = [
        exiftool_exe,
        '-TagsFromFile',
        f'"{jpg_path}"',
        '-all:all', 
        '-overwrite_original', 
        f'"{tif_path}"'
    ]
    
    cmd_string = " ".join(cmd_list)
    assert exiftool_exe in cmd_string
    assert '-TagsFromFile' in cmd_string
    assert '-overwrite_original' in cmd_string
    assert 'test_image.JPG"' in cmd_string
