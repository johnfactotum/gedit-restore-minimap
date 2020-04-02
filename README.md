# Restore Minimap (gedit plugin)

![Screenshot](screenshot.png)

## Features

* Minimap (overview map) was removed in gedit 3.36
* This plugin allows you to have minimap

## Usage

* Open the side panel by pressing F9, or click on the primary menu and choose "View", then check "Side Panel"
* Click on the button on the top of the side panel, and choose "Minimap"

## Installation
```bash
mkdir -p ~/.local/share/gedit/plugins/
cd ~/.local/share/gedit/plugins/
git clone https://github.com/johnfactotum/gedit-restore-minimap.git restore-minimap
```

## Known Issues
* The minimap is now rendered in the side panel, which means:
  * You can't use other side panels and the minimap at the same time.
  * The minimap is displayed on the left, which can be odd.
* It'd be nice if the minimap can use Gnome Builder's block font, but I couldn't figure out how.

## See also
* [Restore Overlay Scrolling](https://github.com/johnfactotum/gedit-restore-overlay-scrolling) - plugin for restoring overlay scrolling, which was also removed in gedit 3.36
* ["Minimap and overlay scrolling disappeared in 3.36"](https://gitlab.gnome.org/GNOME/gedit/issues/285) (discussion of the issue on gedit's issue tracker)
