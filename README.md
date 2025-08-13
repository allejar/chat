# SIPANDA Application

A PyQt5-based desktop application with a modern UI design.

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, execute:
```bash
python main.py
```

## Project Structure

- `main.py` - Main application entry point
- `ui/main_window.py` - Main window controller class
- `ui/ui_main_window.py` - UI design and layout definitions

## Features

- Modern PyQt5-based interface
- Responsive design with custom styling
- Menu bar and toolbar
- Status bar with message display
- Clean, organized code structure

## Troubleshooting

If you encounter the "NameError: name 'self' is not defined" error, ensure that:
1. All method calls using `self` are properly indented within class methods
2. The `__init__` method is properly defined
3. All UI setup code is within the `setupUi` method
