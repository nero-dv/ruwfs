# RUWFS

RUWFS (Random Unsplash Wallpapers for Sway) is a simple program to download, set, and archive wallpapers from Unsplash for your Sway-enabled desktop. 

# Description

This program is a simple script to download, set, and archive wallpapers from Unsplash for your sway desktop. It is written in Python and does not use the Unsplash API to download images <sup>1</sup>. It is designed to be used with sway; RUWFS cannot currently can be used with any other desktop environment that supports setting wallpapers unless that method is by using swaybg. The program is designed to be run as a systemd service, but can be run manually as well <sup>2</sup>.

##### <sup>1</sup> The Unsplash API is rate limited and requires an API key. This program does not use the API and instead uses the Unsplash website to download images. This means that the program is not rate limited and does not require an API key, but it also means that the program is not guaranteed to work in the future if Unsplash changes their website. There is a chance that you may be blocked from downloading images from Unsplash if you run the program manually too many times.

##### <sup>2</sup> The program can be run manually, but it is not recommended. The program is designed to be run as a systemd service <sup><i>[TODO].</i></sup> You should use the provided systemd service file to run the program as a service. 

# Getting Started

## Dependencies

<a href=https://swaywm.org/>Sway</a>: A tiling Wayland compositor and a drop-in replacement for the i3 window manager for X11. It works with your existing i3 configuration and supports most of i3's features, plus a few extras. 

Python 3.7 or higher is needed to run this program. The program requires the following Python module:

<a href=https://requests.readthedocs.io/en/latest/>Requests >= 2.28.0</a>: A simple, yet elegant HTTP library. It provides methods for accessing Web resources via HTTP. It is an Apache2 Licensed HTTP library, written in Python.

To install the Requests library, simply run this simple command in your terminal and virtualenv of choice:

```python
$ python -m pip install requests
```

## Installing RUWFS

* Clone this repository to your computer:

* Run the installer script, or install the service file manually by copying it to your systemd user directory:

## Help

If you have any questions or need help, please feel free to open an issue on the GitHub repository.



## Authors

Contributors names and contact info

* Louis Del Valle <[@looper@mastodon.world](https://mastodon.world/@looper)>


## Version History

* 0.1
    * Initial Release


## License

This project is licensed under the GPLv3 License - see the license.md file for details

