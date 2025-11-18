# core/raw_processor.py
"""
Handles RAW generation using the DJI utility. Provides both synchronous and async wrappers.
Abstracts platform-specific differences (Windows for DJI SDK example).
"""
import os
import subprocess
from utils.logger import get_logger
logger = get_logger(__name__)

def generate_raw_windows(dji_irp_exe: str, working_dir: str) -> bool:
    """
    Uses a for-loop Windows cmd approach to process .JPG files into .raw via dji_irp.exe.
    dji_irp_exe: full path to dji_irp.exe
    working_dir: directory containing .JPG files
    """
    if not os.path.exists(dji_irp_exe):
        logger.error("DJI executable not found: %s", dji_irp_exe)
        return False
    cmd = f'for %i in ("*.JPG") do "{dji_irp_exe}" -a measure -s "%i" -o "%~ni.raw" --measurefmt float32'
    # Launch in new cmd window to allow user to see progress; use shell True for cmd syntax
    try:
        subprocess.Popen(f'start cmd /K "cd /d {working_dir} & {cmd}"', shell=True)
        logger.info("Started DJI RAW generation (Windows cmd): %s", dji_irp_exe)
        return True
    except Exception as e:
        logger.exception("Failed to start DJI RAW generation: %s", e)
        return False

def generate_raw(dji_irp_exe: str, working_dir: str) -> bool:
    """
    Dispatch to appropriate method for the platform. Currently supports Windows primarily.
    """
    if os.name == 'nt':
        return generate_raw_windows(dji_irp_exe, working_dir)
    else:
        logger.error("RAW generation via DJI SDK is currently supported only on Windows in this tool.")
        return False
