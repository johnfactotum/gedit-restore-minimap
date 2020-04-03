# Restore Minimap (gedit plugin)

![Screenshot](screenshot.png)

## Features

* Minimap (overview map) was removed in gedit 3.36
* This plugin allows you to have minimap

## Installation
```bash
mkdir -p ~/.local/share/gedit/plugins/
cd ~/.local/share/gedit/plugins/
git clone https://github.com/johnfactotum/gedit-restore-minimap.git restore-minimap
```

## Known Issues
* The minimap is displayed on the left, which can be a bit odd.
* It'd be nice if the minimap can use Gnome Builder's block font, but I couldn't figure out how.

## See also
* [Restore Overlay Scrolling](https://github.com/johnfactotum/gedit-restore-overlay-scrolling) - plugin for restoring overlay scrolling, which was also removed in gedit 3.36
* [Restore Zen](https://github.com/johnfactotum/gedit-restore-zen) - plugin for restoring zen mode, which was also removed in gedit 3.36
* ["Minimap and overlay scrolling disappeared in 3.36"](https://gitlab.gnome.org/GNOME/gedit/issues/285) (discussion of the issue on gedit's issue tracker)
