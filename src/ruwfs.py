import subprocess
import os
import requests
import json
import time
import random
from pathlib import Path


def main():
    home = Path.home() / ".ruwfs"
    image_dir = home / "images"
    archive_dir = image_dir / "archive"
    tmp_dir = home / "tmp"
    obuffer = tmp_dir / "outputs.json"
    paths = [home, image_dir, archive_dir, tmp_dir]
    output_list = []

    # Create the directories if they don't exist
    for path in paths:
        if not path.exists():
            path.mkdir(parents=True)

    # Move all current images to the archive folder
    for file in image_dir.glob("*.jpg"):
        file.rename(archive_dir / file.name)

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

    try:
        with open(obuffer, "r") as f:
            outputs = json.load(f)
        for i in range(len(outputs)):
            output_list.append(outputs[i]["name"])
        for idx, item in enumerate(output_list):
            random_topic = random.choice(topics)
            image_path = f"{image_dir}/{today()}_{random_topic}_{idx}.jpg"
            response = requests.get(
                f"https://source.unsplash.com/2560x1440/?{random_topic}"
            )
            with open(image_path, "wb") as f:
                f.write(response.content)
            subprocess.call(
                ["swaymsg", "output", item["name"], "bg", image_path, "fill"]
            )
        time.sleep(30 + random.randint(0, 30))
        main()

    except FileNotFoundError:
        subprocess.call(
            ["swaymsg", "-t", "get_outputs", "-r"],
            stdout=open(obuffer, "w"),
            stderr=print(
                "Error trying to get outputs from swaymsg. Is swaymsg installed?"
            ),
        )  # Get the outputs and save them to outputs.json


if __name__ == "__main__":
    main()
