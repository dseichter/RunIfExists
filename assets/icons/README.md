# Icon Assets

This directory contains icon assets for the RunIfExists application.

## Material Symbols

The application uses Google Material Symbols for UI icons:

- **close** - Close/Cancel actions
- **help** - Help and support 
- **refresh** - Update/Refresh actions
- **info** - Information dialogs
- **sports** - Main application icon (track and field theme)

## Usage

Icons are loaded via the `icons_pyside.py` module which:
1. First attempts to load Material Symbols from system theme
2. Falls back to Qt standard icons if Material Symbols unavailable
3. Provides consistent icon interface across platforms

## Adding New Icons

To add new Material Symbol icons:

1. Find the icon name from [Material Symbols](https://fonts.google.com/icons)
2. Add mapping to `MATERIAL_ICONS` dict in `icons_pyside.py`
3. Add property to `MaterialIcons` class
4. Add fallback to `standard_icons` dict if needed

## Custom Icons

For custom icons, place SVG files in this directory and load via:

```python
icon = QIcon(os.path.join('assets', 'icons', 'custom_icon.svg'))
```