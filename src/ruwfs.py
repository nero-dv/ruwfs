import subprocess
import os
import requests
import json
import time
import random


def main():
    data_dir = os.environ["HOME"] + ".ruwfs"
    tmp_dir = data_dir + "/tmp"
    image_dir = data_dir + "/images"
    archive_dir = image_dir + "/archive"

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
    # cwd = os.getcwd()
    obuffer = f"{tmp_dir}/outputs.json"
    files = os.listdir(f"{image_dir}")

    # Move all current images to the archive folder
    for idx, file in enumerate(files):
        if file.endswith(".jpg"):
            subprocess.run(["mv", f"{image_dir}/{file}", f"{archive_dir}/{file}"])

    try:
        with open(obuffer, "r") as f:
            outputs = json.load(f)
        for idx, item in enumerate(outputs):
            random_topic = random.choice(topics)
            image_path = f"{image_dir}/{today()}_{random_topic}_{idx}.jpg"
            # print(f"Setting image {image_path} as wallpaper for {output_string}")
            response = requests.get(
                f"https://source.unsplash.com/2560x1440/?{random_topic}"
            )
            with open(image_path, "wb") as f:
                f.write(response.content)
            subprocess.call(
                ["swaymsg", "output", item["name"], "bg", image_path, "fill"]
            )
        # time.sleep(86400)
        # main()

    except FileNotFoundError:
        subprocess.call(
            ["swaymsg", "-t", "get_outputs", "-r"],
            stdout=open(f"{tmp_dir}/outputs.json", "w"),
            stderr=print(
                "Error trying to get outputs from swaymsg. Is swaymsg installed?"
            ),
        )  # Get the outputs and save them to outputs.json


if __name__ == "__main__":
    main()
