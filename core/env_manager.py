# core/env_manager.py
"""
Functions to manage and validate environment dependencies:
- Check DJI utility presence
- Check ImageJ executable
- Check ExifTool executable
"""
import os
from utils.logger import get_logger
logger = get_logger(__name__)

def validate_dji(dji_folder: str) -> bool:
    exe = os.path.join(dji_folder, 'dji_irp.exe')
    ok = os.path.exists(exe)
    logger.debug("validate_dji: %s -> %s", exe, ok)
    return ok

def validate_imagej(imagej_exe: str) -> bool:
    ok = imagej_exe and os.path.exists(imagej_exe)
    logger.debug("validate_imagej: %s -> %s", imagej_exe, ok)
    return ok

def validate_exiftool(exiftool_cmd: str) -> bool:
    # Accept either 'exiftool' on PATH or a full path
    ok = False
    if os.path.isabs(exiftool_cmd):
        ok = os.path.exists(exiftool_cmd)
    else:
        # try find in PATH
        for p in os.environ.get("PATH", "").split(os.pathsep):
            candidate = os.path.join(p, exiftool_cmd)
            if os.path.exists(candidate):
                ok = True
                break
    logger.debug("validate_exiftool: %s -> %s", exiftool_cmd, ok)
    return ok
