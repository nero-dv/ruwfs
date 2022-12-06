import subprocess
import os
import requests
import json
import time
import random

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


def main():
    # Get yesterday's date for archive
    # yday = time.strftime("%Y-%m-%d", time.localtime(time.time() - 86400))
    # Get today's date and time for current images
    def today():
        return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

    # List of topics to iterate through
    topics = [
        "space",
        "nature",
        "water",
        "mountains",
        "city",
        "beach",
        "forest",
        "ocean",
        "sky",
        "desert",
        "snow",
        "sunset",
        "sunrise",
        "night",
        "stars",
        "clouds",
        "rain",
        "lightning",
        "snow",
        "fire",
        "animals",
        "art",
        "architecture",
        "travel",
        "history",
    ]

    # Get the current working directory
    cwd = os.getcwd()
    obuffer = f"{cwd}/tmp/outputs.json"
    files = os.listdir(f"{cwd}/images")

    # Move all current images to the archive folder
    for idx, file in enumerate(files):
        if file.endswith(".jpg"):
            subprocess.run(["mv", f"{cwd}/images/{file}", f"{cwd}/archive/{file}"])

    try:
        with open(obuffer, "r") as f:
            outputs = json.load(f)
        for idx, item in enumerate(outputs):
            random_topic = random.choice(topics)
            image_path = f"{cwd}/images/{today()}_{random_topic}_{idx}.jpg"
            # print(f"Setting image {image_path} as wallpaper for {output_string}")
            response = requests.get(
                f"https://source.unsplash.com/2560x1440/?{random_topic}"
            )
            with open(image_path, "wb") as f:
                f.write(response.content)
            subprocess.call(
                ["swaymsg", "output", item["name"], "bg", image_path, "fill"]
            )
            # time.sleep(2)

    except FileNotFoundError:
        subprocess.call(
            ["swaymsg", "-t", "get_outputs", "-r"],
            stdout=open(f"{cwd}/tmp/outputs.json", "w"),
            stderr=print(
                "Error trying to get outputs from swaymsg. Is swaymsg installed?"
            ),
        )  # Get the outputs and save them to outputs.json


if __name__ == "__main__":
    main()
