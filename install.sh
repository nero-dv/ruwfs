#!/bin/env bash

# RUWFS (Random Unsplash Wallpapers for Sway) is a simple program to download, set, and archive wallpapers from Unsplash for your Sway-enabled desktop.

# Copyright (C) 2022  Louis Del Valle - louis[at]louisdelvalle.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


command_exists() {
  command -v "$@" >/dev/null 2>&1
}

HOME="/home/$USER"
RUWFS_DIR="$HOME/.ruwfs"

command_exists sway || { echo "Sway is not installed. Please install Sway before running this script."; exit 1;}
command_exists git || { echo "git is not installed"; exit 1;}
command_exists pip3 || { echo "pip3 is not installed"; exit 1;}
command_exists python3 || { echo "python3 is not installed"; exit 1;}


git clone https://github.com/nero-dv/ruwfs "${RUWFS_DIR}" && cd "${RUWFS_DIR}"
chown -R $USER:$USER $RUWFS_DIR

if [ -f $HOME/.config/sway/config ]; then
    echo "Sway config file found. Removing current bg configuration and directory for custom configuration."
    sed -i '/output \* bg/d' $HOME/.config/sway/config
    mkdir -p $HOME/.config/sway/backgrounds
    echo "include $HOME/.config/sway/backgrounds/*.conf" >> $HOME/.config/sway/config
    echo "exec_always --no-startup-id python ~/.ruwfs/src/ruwfs.py" >> $HOME/.config/sway/config/backgrounds/ruwfs.conf
    echo
    echo "Background configuration added to Sway config file."
    echo "Reload your config file to start using RUWFS."
fi