#!/usr/bin/env python3
"""
Colors Module for BloodRecon Tool
Centralized color management for consistent styling across all modules
Author : Alex Butler (@VritraSecz)
Org    : Vritra Security Organization
"""

from colorama import Fore, Back, Style, init

init(autoreset=True)

BLACK = Fore.BLACK
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE

LIGHTBLACK_EX = Fore.LIGHTBLACK_EX
LIGHTRED_EX = Fore.LIGHTRED_EX
LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
LIGHTYELLOW_EX = Fore.LIGHTYELLOW_EX
LIGHTBLUE_EX = Fore.LIGHTBLUE_EX
LIGHTMAGENTA_EX = Fore.LIGHTMAGENTA_EX
LIGHTCYAN_EX = Fore.LIGHTCYAN_EX
LIGHTWHITE_EX = Fore.LIGHTWHITE_EX

BG_BLACK = Back.BLACK
BG_RED = Back.RED
BG_GREEN = Back.GREEN
BG_YELLOW = Back.YELLOW
BG_BLUE = Back.BLUE
BG_MAGENTA = Back.MAGENTA
BG_CYAN = Back.CYAN
BG_WHITE = Back.WHITE

BG_LIGHTBLACK_EX = Back.LIGHTBLACK_EX
BG_LIGHTRED_EX = Back.LIGHTRED_EX
BG_LIGHTGREEN_EX = Back.LIGHTGREEN_EX
BG_LIGHTYELLOW_EX = Back.LIGHTYELLOW_EX
BG_LIGHTBLUE_EX = Back.LIGHTBLUE_EX
BG_LIGHTMAGENTA_EX = Back.LIGHTMAGENTA_EX
BG_LIGHTCYAN_EX = Back.LIGHTCYAN_EX
BG_LIGHTWHITE_EX = Back.LIGHTWHITE_EX

RESET_ALL = Style.RESET_ALL
BRIGHT = Style.BRIGHT
DIM = Style.DIM
NORMAL = Style.NORMAL

SUCCESS = GREEN
ERROR = RED
WARNING = YELLOW
INFO = CYAN
DEBUG = MAGENTA

BANNER = CYAN
MENU_HEADER = YELLOW
MENU_OPTION = GREEN
MENU_TEXT = WHITE
INPUT_PROMPT = CYAN
INPUT_EXAMPLE = YELLOW

TOOL_NAME = MAGENTA
VERSION_INFO = GREEN
AUTHOR_INFO = WHITE
WARNING_TEXT = RED
SEPARATOR = CYAN

DATA_LABEL = YELLOW
DATA_VALUE = WHITE
DATA_SUCCESS = GREEN
DATA_ERROR = RED
DATA_HIGHLIGHT = CYAN

IP_COLOR = LIGHTCYAN_EX
DOMAIN_COLOR = LIGHTGREEN_EX
URL_COLOR = LIGHTBLUE_EX
EMAIL_COLOR = LIGHTYELLOW_EX
PHONE_COLOR = LIGHTMAGENTA_EX

FOUND = GREEN
NOT_FOUND = RED
PARTIAL = YELLOW
UNKNOWN = MAGENTA


def colored_text(text, color, style=None):
    """
    Apply color and optional style to text
    
    Args:
        text (str): Text to colorize
        color (str): Color code
        style (str, optional): Style code
    
    Returns:
        str: Colored text
    """
    if style:
        return f"{style}{color}{text}{RESET_ALL}"
    return f"{color}{text}{RESET_ALL}"

def success_text(text):
    """Return text in success color"""
    return colored_text(text, SUCCESS)

def error_text(text):
    """Return text in error color"""
    return colored_text(text, ERROR)

def warning_text(text):
    """Return text in warning color"""
    return colored_text(text, WARNING)

def info_text(text):
    """Return text in info color"""
    return colored_text(text, INFO)

def highlight_text(text):
    """Return text in highlight color with bright style"""
    return colored_text(text, DATA_HIGHLIGHT, BRIGHT)

def banner_text(text):
    """Return text in banner color"""
    return colored_text(text, BANNER)

def menu_header_text(text):
    """Return text in menu header color"""
    return colored_text(text, MENU_HEADER)

def menu_option_text(text):
    """Return text in menu option color"""
    return colored_text(text, MENU_OPTION)

def input_prompt_text(text):
    """Return text in input prompt color"""
    return colored_text(text, INPUT_PROMPT)

def input_example_text(text):
    """Return text in input example color"""
    return colored_text(text, INPUT_EXAMPLE)

# ============================================================================
# FORMATTED OUTPUT FUNCTIONS
# ============================================================================

def print_success(message):
    """Print success message"""
    print(success_text(f"[✓] {message}"))

def print_error(message):
    """Print error message"""
    print(error_text(f"[✗] {message}"))

def print_warning(message):
    """Print warning message"""
    print(warning_text(f"[!] {message}"))

def print_info(message):
    """Print info message"""
    print(info_text(f"[i] {message}"))

def print_separator(char="=", length=80):
    """Print colored separator line"""
    print(colored_text(char * length, SEPARATOR))

def print_header(title, width=80):
    """Print formatted header"""
    padding = (width - len(title) - 2) // 2
    header = f"{'=' * padding} {title} {'=' * padding}"
    if len(header) < width:
        header += "="
    print(colored_text(header, BANNER))

# ============================================================================
# EXPORT ALL COLORS AND FUNCTIONS
# ============================================================================

__all__ = [
    # Basic Colors
    'BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE',
    # Light Colors
    'LIGHTBLACK_EX', 'LIGHTRED_EX', 'LIGHTGREEN_EX', 'LIGHTYELLOW_EX',
    'LIGHTBLUE_EX', 'LIGHTMAGENTA_EX', 'LIGHTCYAN_EX', 'LIGHTWHITE_EX',
    # Background Colors
    'BG_BLACK', 'BG_RED', 'BG_GREEN', 'BG_YELLOW', 'BG_BLUE', 'BG_MAGENTA', 'BG_CYAN', 'BG_WHITE',
    'BG_LIGHTBLACK_EX', 'BG_LIGHTRED_EX', 'BG_LIGHTGREEN_EX', 'BG_LIGHTYELLOW_EX',
    'BG_LIGHTBLUE_EX', 'BG_LIGHTMAGENTA_EX', 'BG_LIGHTCYAN_EX', 'BG_LIGHTWHITE_EX',
    # Styles
    'RESET_ALL', 'BRIGHT', 'DIM', 'NORMAL',
    # Status Colors
    'SUCCESS', 'ERROR', 'WARNING', 'INFO', 'DEBUG',
    # UI Colors
    'BANNER', 'MENU_HEADER', 'MENU_OPTION', 'MENU_TEXT', 'INPUT_PROMPT', 'INPUT_EXAMPLE',
    # Tool Colors
    'TOOL_NAME', 'VERSION_INFO', 'AUTHOR_INFO', 'WARNING_TEXT', 'SEPARATOR',
    # Data Colors
    'DATA_LABEL', 'DATA_VALUE', 'DATA_SUCCESS', 'DATA_ERROR', 'DATA_HIGHLIGHT',
    # Network Colors
    'IP_COLOR', 'DOMAIN_COLOR', 'URL_COLOR', 'EMAIL_COLOR', 'PHONE_COLOR',
    # Result Colors
    'FOUND', 'NOT_FOUND', 'PARTIAL', 'UNKNOWN',
    # Utility Functions
    'colored_text', 'success_text', 'error_text', 'warning_text', 'info_text',
    'highlight_text', 'banner_text', 'menu_header_text', 'menu_option_text',
    'input_prompt_text', 'input_example_text',
    # Print Functions
    'print_success', 'print_error', 'print_warning', 'print_info',
    'print_separator', 'print_header'
]