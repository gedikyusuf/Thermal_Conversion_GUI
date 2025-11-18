# thermal_converter/exceptions.py
"""Custom exception classes for the Thermal Conversion Utility."""

class ThermalConverterError(Exception):
    """Base exception class for all custom errors in the application."""
    def __init__(self, message="A general error occurred in the Thermal Converter."):
        super().__init__(message)
        self.code = 100

class PathInitializationError(ThermalConverterError):
    """Raised when the root folder is invalid or necessary external tool paths cannot be configured."""
    def __init__(self, root_path, required_path):
        message = (
            f"Required path '{required_path}' could not be initialized based on root folder '{root_path}'. "
            "Please check the folder structure."
        )
        super().__init__(message)
        self.code = 101

class MissingDependencyError(ThermalConverterError):
    """Raised when a critical external executable (dji_irp.exe, ImageJ, or ExifTool) is missing."""
    def __init__(self, dependency_name, expected_path):
        message = (
            f"Dependency '{dependency_name}' is missing. Expected path: {expected_path}. "
            "Ensure the necessary software is installed and the root folder is correct."
        )
        super().__init__(message)
        self.code = 102

class CommandExecutionError(ThermalConverterError):
    """Raised when an external subprocess command fails to execute or returns a non-zero exit code."""
    def __init__(self, command, error_detail):
        message = (
            f"External command execution failed. Command: {command}. "
            f"Details: {error_detail}"
        )
        super().__init__(message)
        self.code = 103
