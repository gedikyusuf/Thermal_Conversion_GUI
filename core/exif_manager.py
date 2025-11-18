# core/exif_manager.py
"""
Handles exiftool calls to copy tags from original JPG to converted TIFF.
Assumes exiftool is available on PATH or provided as full path.
"""
import os
import subprocess
from utils.logger import get_logger
logger = get_logger(__name__)

def copy_exif_tags(exiftool_cmd: str, jpg_path: str, tif_path: str) -> bool:
    cmd = [exiftool_cmd, '-TagsFromFile', jpg_path, '-all:all', '-overwrite_original', tif_path]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        logger.debug("ExifTool stdout: %s", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        logger.error("ExifTool error: %s", e.stderr)
        return False

def batch_copy_tags(exiftool_cmd: str, src_folder: str, dest_folder: str):
    jpgs = [f for f in os.listdir(src_folder) if f.lower().endswith('.jpg')]
    for jpg in jpgs:
        jpg_path = os.path.join(src_folder, jpg)
        tif_name = os.path.splitext(jpg)[0] + '.TIF'
        tif_path = os.path.join(dest_folder, tif_name)
        if os.path.exists(tif_path):
            copy_exif_tags(exiftool_cmd, jpg_path, tif_path)
        else:
            logger.warning("Expected TIFF not found for %s", jpg)
