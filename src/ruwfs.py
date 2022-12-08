import subprocess
import os
import requests
import json
import time
import random
from pathlib import Path


def main():
    # Get today's date and time for current images
    def today():
        return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

    # Set topics
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
    # Get paths
    def paths():
        home = Path.home() / ".ruwfs"
        image_dir = home / "images"
        archive_dir = image_dir / "archive"
        tmp_dir = home / "tmp"
        paths = [home, image_dir, archive_dir, tmp_dir]

        for path in paths:
            if not path.exists():
                path.mkdir(parents=True)

        return paths

    paths = paths()

    # Get outputs from swaymsg
    output_list = []
    obuffer = paths[3] / "outputs.json"
    cached_outputs = paths[3] / "cached_outputs.json"

    def archive_images():
        # Move all current images to the archive folder
        for file in paths[1].glob("*.jpg"):
            file.rename(paths[2] / file.name)

    def get_outputs():
        # If the outputs.json file is empty or doesn't exist, get outputs from swaymsg
        if not obuffer.is_file() or obuffer.stat().st_size == 0:
            print("obuffer doesn't exist or is empty")
            print("Creating obuffer file")
            create_obuffer = subprocess.run(
                ["swaymsg", "-t", "get_outputs", "-r"],
                check=True,
            )
            if create_obuffer.returncode == 0:
                with open(obuffer, "w") as f:
                    json.dump(create_obuffer.stdout, f)
                print("obuffer file created")
            elif create_obuffer.returncode != 0:
                buffer_error = create_obuffer.stderr
                print("Error trying to get outputs from swaymsg. Is swaymsg installed?")
                print("Writing error to log file")
                with open(paths[3] / "ruwfs.log", "a") as f:
                    f.write(buffer_error)
                print("Exiting. . .")
                exit(1)
        else:
            print("obuffer exists and is not empty")

        print("Creating cached_outputs.json from obuffer")
        # Load outputs from outputs.json
        with open(obuffer, "r") as f:
            outputs = json.load(f)
        # Get the name of each output and append it to output_list
        for idx in range(len(outputs)):
            output_list.append(outputs[idx]["name"])
        # Write output_list to cached_outputs.json for future use
        with open(cached_outputs, "w") as ff:
            json.dump(output_list, ff)

    # If the cached_outputs.json file is empty or doesn't exist:
    # Get outputs from swaymsg
    # Write the filtered list to cached_outputs.json
    if not cached_outputs.is_file() or cached_outputs.stat().st_size == 0:
        print(f"{cached_outputs} doesn't exist or is empty")
        print("Checking for obuffer file")
        get_outputs()

    # Load cached_outputs.json
    with open(cached_outputs, "r") as fff:
        output_list = json.load(fff)

    def get_images():
        # Archive current images before requesting new ones
        archive_images()
        image_list = []
        # Request an image with a random topic
        for idx in range(len(output_list)):
            random_topic = random.choice(topics)
            image_path = f"{paths[1]}/{today()}_{random_topic}_{idx}.jpg"
            unsplash_image = requests.get(
                f"https://source.unsplash.com/2560x1440/?{random_topic}"
            )
            with open(image_path, "wb") as f:
                f.write(unsplash_image.content)
            image_list.append(image_path)

        return image_list

    def set_backgrounds():
        # Get a random image for each monitor
        image_list = get_images()
        # Set the background for each monitor
        for idx, image in enumerate(image_list):
            subprocess.call(
                ["swaymsg", "output", output_list[idx], "bg", image_list[idx], "fill"]
            )
        time.sleep(10)
        set_backgrounds()

    set_backgrounds()

    # while True:
    #     # time.sleep(30 + random.randint(0, 30))
    #     time.sleep(10)
    #     set_backgrounds()


if __name__ == "__main__":
    main()
