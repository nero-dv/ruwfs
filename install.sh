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

# setup_color() {
#   FMT_RED=$(printf '\033[31m')
#   FMT_GREEN=$(printf '\033[32m')
#   FMT_YELLOW=$(printf '\033[33m')
#   FMT_BLUE=$(printf '\033[34m')
#   FMT_BOLD=$(printf '\033[1m')
#   FMT_RESET=$(printf '\033[0m')
# }
# setup_color

command_exists() {
  command -v "$@" >/dev/null 2>&1
}

# fmt_error() {
#   printf '%sError: %s%s\n' "${FMT_BOLD}${FMT_RED}" "$*" "$FMT_RESET" >&2
# }

HOME="/home/$USER"
RUWFS_DIR="$HOME/.ruwfs"

if [ ! -d "$RUWFS_DIR" ]; then
    echo "Creating directory $RUWFS_DIR"
    mkdir -p ${RUWFS_DIR}
    mkdir -p ${RUWFS_DIR}/images/archive
    mkdir -p ${RUWFS_DIR}/tmp
    touch ${RUWFS_DIR}/tmp/install.log
fi

command_exists sway || { echo "Sway is not installed. Please install Sway before running this script."; exit 1;}
command_exists git || { echo "git is not installed"; exit 1;}
command_exists pip3 || { echo "pip3 is not installed"; exit 1;}
command_exists python3 || { echo "python3 is not installed"; exit 1;}


git clone --max-depth=1 https://github.com/nero-dv/ruwfs $RUWFS_DIR && cd $RUWFS_DIR
chown -R $USER:$USER $RUWFS_DIR

if [ -f $HOME/.config/sway/config ]; then
    sed -i '/output \* bg/d' $HOME/.config/sway/config
    echo "exec_always --no-startup-id python ~/.ruwfs/ruwfs.py" >> $HOME/.config/sway/config
fi




