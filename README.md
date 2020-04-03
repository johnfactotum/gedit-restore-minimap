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

To use Gnome Builder's block font, which makes the minimap looks so much better that I wonder why they haven't bundled the font with gtksourceview itself, copy `BuilderBlocks.ttf` to `~/.local/share/fonts`.

## Configuration

You can display the minimap on the left by deleting line 15 in `restore_minimap.py`:
```python
# move the minimap to the right
self.tab.set_direction(Gtk.TextDirection.RTL)
```

## Known Issues
* It'd be nice if the minimap can use Gnome Builder's block font without having to install it, but I couldn't figure out how
* There's currently no way to configure the minimap except editing the source code

## See also
* [Restore Overlay Scrolling](https://github.com/johnfactotum/gedit-restore-overlay-scrolling) - plugin for restoring overlay scrolling, which was also removed in gedit 3.36
* [Restore Zen](https://github.com/johnfactotum/gedit-restore-zen) - plugin for restoring zen mode, which was also removed in gedit 3.36
* ["Minimap and overlay scrolling disappeared in 3.36"](https://gitlab.gnome.org/GNOME/gedit/issues/285) (discussion of the issue on gedit's issue tracker)
