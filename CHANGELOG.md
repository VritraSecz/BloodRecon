# Changelog

All notable changes to BloodRecon will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-07-31

### 🎉 What's New

#### Enhanced Shodan Integration
- **New Command Line API Management**: Set Shodan API keys directly from command line without interactive mode
- **Streamlined Configuration**: Unified config system using `~/.config-vritrasecz/bloodrecon-shodan.json`
- **Improved API Key Handling**: Automatic key validation and replacement functionality

### ✨ Added
- **`--shodan-api` Argument**: New command line option to set Shodan API key non-interactively
  ```bash
  python3 bloodrecon.py --shodan-api "your_api_key_here"
  ```
- **Enhanced Config Directory Structure**: Organized configuration in `~/.config-vritrasecz/` directory
- **Automatic Directory Creation**: Tool automatically creates config directories if they don't exist
- **JSON-Only Configuration**: Simplified config management using only JSON format
- **API Key Replacement**: New API keys automatically replace existing ones in config file
- **Input Validation**: Enhanced validation for empty or invalid API keys
- **Improved Error Handling**: Better error messages and handling for API key operations

### 🔧 Improved
- **Shodan Module Architecture**: Refactored for better maintainability and performance
- **Configuration Management**: Streamlined API key loading and saving processes
- **User Experience**: Cleaner output and more intuitive API key management
- **Code Organization**: Better separation of concerns in API key handling functions

### 🗑️ Removed
- **config.py API Storage**: Removed dual config.py file saving for simplified management
- **Legacy Config Paths**: Removed old `~/.osint_shodan_config` file references
- **Redundant Functions**: Cleaned up unused config.py save functionality

### 🔄 Changed
- **Config File Location**: Moved from `~/.osint_shodan_config` to `~/.config-vritrasecz/bloodrecon-shodan.json`
- **API Key Storage**: Now saves only to JSON format for consistency
- **Version Number**: Updated from 1.0 to 1.2.0 to reflect significant improvements

### 🐛 Fixed
- **API Key Persistence**: Resolved issues with API key not being properly saved
- **Interactive Mode Conflicts**: Fixed conflicts between command line and interactive API key setting
- **Error Message Clarity**: Improved error messages for better user understanding

### 📚 Technical Details

#### New Functions Added:
- `set_shodan_api_key(api_key)`: Direct API key setting without interactive mode
- Enhanced `save_api_key()`: Improved JSON-only saving functionality
- Updated `load_api_key()`: Streamlined API key loading process

#### Configuration Changes:
- **Primary Config**: `~/.config-vritrasecz/bloodrecon-shodan.json`
- **Fallback Support**: Still supports environment variables and existing config.py files
- **Auto-migration**: Automatically handles existing configurations

#### Command Line Interface:
```bash
# Set API key
python3 bloodrecon.py --shodan-api "your_api_key"

# Use Shodan with saved key
python3 bloodrecon.py --shodan 8.8.8.8

# View help
python3 bloodrecon.py --help
```

### 🎯 Benefits for Users

1. **Simplified Setup**: One command to set up Shodan integration
2. **Better Organization**: Clean config directory structure
3. **Improved Reliability**: More robust API key management
4. **Enhanced Security**: Better validation and error handling
5. **Streamlined Workflow**: No more interactive prompts for API key setup

### 🔮 Looking Forward

This update lays the foundation for:
- Additional API integrations with similar streamlined setup
- Enhanced configuration management for other services
- Improved user experience across all modules

---

## [1.0.0] - 2025-07-28

### Initial Release
- Complete OSINT framework with 34+ specialized modules
- Interactive CLI interface
- Comprehensive reconnaissance capabilities
- Cross-platform compatibility
- Educational and authorized testing focus

---

**Note**: This changelog documents significant changes and improvements. For detailed technical information, please refer to the module documentation and source code comments.
