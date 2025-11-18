# utils/file_utils.py
"""
File-related helper functions: safe copy, enumerate images, create folders, extension helpers.
"""
import os
import shutil
from typing import List

def ensure_dir(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path

def list_images(folder: str, exts=None) -> List[str]:
    if exts is None:
        exts = {'.jpg', '.jpeg', '.JPG', '.JPEG', '.tif', '.tiff', '.TIF', '.TIFF'}
    files = []
    for f in os.listdir(folder):
        if os.path.splitext(f)[1] in exts:
            files.append(f)
    return sorted(files)

def safe_copy(src: str, dst: str, overwrite: bool=False):
    ensure_parent = os.path.dirname(dst)
    os.makedirs(ensure_parent, exist_ok=True)
    if overwrite and os.path.exists(dst):
        os.remove(dst)
    shutil.copy2(src, dst)
    return dst
