# core/tiff_converter.py
"""
Simple wrapper to handle post-processing of ImageJ output, moving files to output folder,
optional bit-depth promotion or reprojection routines can be added here.
"""
import os
import glob
from utils.logger import get_logger
logger = get_logger(__name__)

def collect_converted_tifs(src_folder: str, dest_folder: str, pattern="*.TIF"):
    os.makedirs(dest_folder, exist_ok=True)
    files = glob.glob(os.path.join(src_folder, pattern))
    moved = []
    for f in files:
        name = os.path.basename(f)
        dst = os.path.join(dest_folder, name)
        try:
            os.replace(f, dst)
            moved.append(dst)
        except Exception:
            # fallback copy
            import shutil
            shutil.copy2(f, dst)
            moved.append(dst)
    logger.info("Collected %d converted TIFFs into %s", len(moved), dest_folder)
    return moved
