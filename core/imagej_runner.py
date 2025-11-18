# core/imagej_runner.py
"""
Runs ImageJ in headless mode with a macro. Copies macro to temp, constructs args.
"""
import os
import subprocess
import tempfile
from utils.logger import get_logger
logger = get_logger(__name__)

def run_imagej_macro(imagej_executable: str, macro_file: str, macro_args: str, timeout: int = 600):
    """
    Run ImageJ headless with macro.
    macro_args is a single string the macro expects (customize macro accordingly).
    Returns (returncode, stdout, stderr)
    """
    if not imagej_executable or not os.path.exists(imagej_executable):
        raise FileNotFoundError(f"ImageJ executable not found: {imagej_executable}")

    tmp_macro = os.path.join(tempfile.gettempdir(), os.path.basename(macro_file))
    try:
        # copy macro to temp (ensures write access if macro modifies files)
        import shutil
        shutil.copy2(macro_file, tmp_macro)
    except Exception as e:
        logger.warning("Could not copy macro to temp: %s", e)
        tmp_macro = macro_file

    cmd = [imagej_executable, "--headless", "-macro", tmp_macro, macro_args]
    logger.info("Running ImageJ macro: %s", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    logger.debug("ImageJ stdout: %s", result.stdout)
    logger.debug("ImageJ stderr: %s", result.stderr)
    return result.returncode, result.stdout, result.stderr
